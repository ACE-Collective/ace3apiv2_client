"""live smoke test for aceapi-v2-client

this test talks to a running ACE API v2 instance. it is skipped unless the
``ACE_API_BASE_URL`` and ``ACE_API_KEY`` environment variables are set, so it
never blocks installs or offline test runs.

api keys are scoped, so the key you point this at matters. the ping and
``/users/me*`` tests only need a valid key; the rest additionally need the
matching read scope (``observable:read``, ``alert:read``, ``event:read`` ...).
an inherit-scoped key belonging to a privileged user satisfies all of them.

example:
    ACE_API_BASE_URL=https://ace-http/api/v2 \\
    ACE_API_KEY=60eeab2c-aced-47a5-b9a5-fd47c8c927b5 \\
    ACE_API_VERIFY_SSL=false \\
    pytest tests/test_smoke.py -v
"""

import os

import pytest

from aceapi_v2_client.auth import authenticated_client
from aceapi_v2_client.api.health import ping_health_ping_get
from aceapi_v2_client.api.common import ping_common_ping_get
from aceapi_v2_client.api.crashes import list_crash_reports_crashes_get
from aceapi_v2_client.api.events import export_events_events_export_get
from aceapi_v2_client.api.observables import (
    list_observable_types_observable_types_get,
    lookup_observables_observables_lookup_post,
)
from aceapi_v2_client.api.saved_filters import (
    create_saved_filter_saved_filters_post,
    delete_saved_filter_saved_filters_filter_uuid_delete,
    get_saved_filter_saved_filters_filter_uuid_get,
    list_saved_filters_saved_filters_get,
    update_saved_filter_saved_filters_filter_uuid_patch,
)
from aceapi_v2_client.api.search import search_alerts_search_alerts_post
from aceapi_v2_client.api.users import (
    get_me_users_me_get,
    get_preferences_users_me_preferences_get,
    list_my_api_keys_users_me_apikeys_get,
)
from aceapi_v2_client.models import (
    AlertSearchRequest,
    ExportFormat,
    FilterEntry,
    LookupPair,
    ObservableLookupRequest,
    SavedFilterCreate,
    SavedFilterUpdate,
)

BASE_URL = os.environ.get("ACE_API_BASE_URL")
API_KEY = os.environ.get("ACE_API_KEY")
VERIFY_SSL = os.environ.get("ACE_API_VERIFY_SSL", "true").lower() not in (
    "0",
    "false",
    "no",
)

pytestmark = pytest.mark.skipif(
    not (BASE_URL and API_KEY),
    reason="set ACE_API_BASE_URL and ACE_API_KEY to run the live smoke test",
)


@pytest.fixture
def client():
    return authenticated_client(BASE_URL, API_KEY, verify_ssl=VERIFY_SSL)


def test_health_ping(client):
    # health/ping requires no auth but should work with a client too
    result = ping_health_ping_get.sync(client=client)
    assert result is not None
    assert result.result == "pong"


def test_common_ping_authenticated(client):
    # common/ping requires authentication; a 200 confirms the api key works
    response = ping_common_ping_get.sync_detailed(client=client)
    assert response.status_code == 200


def test_list_observable_types(client):
    # exercises a real data endpoint that returns parsed models. this endpoint is
    # permission-gated on observable:read, so a narrowly scoped key gets a 403
    # here even though the preceding tests pass.
    response = list_observable_types_observable_types_get.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.parsed is not None


def test_list_my_api_keys(client):
    # self-service key listing: metadata only, never the secret. needs no
    # particular scope, so it doubles as a check that the key itself is live.
    response = list_my_api_keys_users_me_apikeys_get.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    for key in response.parsed:
        # the plaintext key is display-once at creation and must never come back
        assert not hasattr(key, "api_key")


def test_get_me(client):
    # resolves the key back to its owning user
    response = get_me_users_me_get.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.username


def test_get_preferences(client):
    # the whole preference set, defaults included -- a fresh user has never
    # written one, so the payload is the catalog's defaults rather than empty
    response = get_preferences_users_me_preferences_get.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.data is not None


def test_search_alerts(client):
    # the query language endpoint. an instance with no alerts still answers 200
    # with an empty result set, so this asserts the response shape, not content.
    response = search_alerts_search_alerts_post.sync_detailed(
        client=client, body=AlertSearchRequest(query="alert_date:-7d")
    )
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.results is not None


def test_observable_lookup(client):
    # bulk observable lookup; an observable ACE has never seen is still a valid
    # request and comes back with an empty result for that pair
    body = ObservableLookupRequest(
        observables=[LookupPair(type_="ipv4", value="192.0.2.1")]
    )
    response = lookup_observables_observables_lookup_post.sync_detailed(
        client=client, body=body
    )
    assert response.status_code == 200
    assert response.parsed is not None


def test_list_crash_reports(client):
    response = list_crash_reports_crashes_get.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.parsed is not None


def test_export_events_returns_text(client):
    # /events/export serves text/csv, not json. the generated client parses it
    # into a str -- if this ever comes back as None, the generator has dropped
    # the response again (see content_type_overrides in the generator config).
    response = export_events_events_export_get.sync_detailed(
        client=client, type_=ExportFormat.CSV
    )
    assert response.status_code == 200
    assert isinstance(response.parsed, str)


def test_saved_filter_round_trip(client):
    # exercises create/read/update/delete against a real instance, then cleans up
    created = create_saved_filter_saved_filters_post.sync_detailed(
        client=client,
        body=SavedFilterCreate(
            name="aceapi-v2-client smoke test",
            filters=[FilterEntry(name="Disposition", values=["DELIVERY"])],
        ),
    )
    assert created.status_code == 201
    assert created.parsed is not None
    filter_uuid = created.parsed.uuid

    try:
        fetched = get_saved_filter_saved_filters_filter_uuid_get.sync_detailed(
            client=client, filter_uuid=filter_uuid
        )
        assert fetched.status_code == 200
        assert fetched.parsed.name == "aceapi-v2-client smoke test"

        updated = update_saved_filter_saved_filters_filter_uuid_patch.sync_detailed(
            client=client,
            filter_uuid=filter_uuid,
            body=SavedFilterUpdate(description="written by the smoke test"),
        )
        assert updated.status_code == 200
        assert updated.parsed.description == "written by the smoke test"

        listed = list_saved_filters_saved_filters_get.sync_detailed(client=client)
        assert listed.status_code == 200
        assert any(f.uuid == filter_uuid for f in listed.parsed.data)
    finally:
        deleted = delete_saved_filter_saved_filters_filter_uuid_delete.sync_detailed(
            client=client, filter_uuid=filter_uuid
        )
        assert deleted.status_code == 204
