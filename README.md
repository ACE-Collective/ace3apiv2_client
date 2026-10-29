# aceapi-v2-client

A Python client library for the **ACE (Analysis Correlation Engine) API v2**.

The client is generated from the API's OpenAPI schema with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client),
so every endpoint and model is fully typed. A small hand-written `auth` module
adds convenience helpers for ACE's API-key authentication.

## Installation

```bash
pip install aceapi-v2-client
```

Or install from a checkout of this directory:

```bash
pip install .
```

Requires Python 3.9+.

## Quickstart (API key)

ACE's primary machine-to-machine authentication is an API key sent in the
`x-ace-auth` header. Use the `authenticated_client` helper to build a client
with that header pre-populated:

```python
from aceapi_v2_client.auth import authenticated_client
from aceapi_v2_client.api.common import ping_common_ping_get
from aceapi_v2_client.api.observables import (
    list_observable_types_observable_types_get,
)

client = authenticated_client(
    base_url="https://localhost:8443/api/v2",
    api_key="YOUR-API-KEY",
    verify_ssl=False,  # development instances use a self-signed certificate
)

# a simple authenticated health check
pong = ping_common_ping_get.sync(client=client)
print(pong.result)  # "pong"

# call a data endpoint — responses are parsed into typed models
types = list_observable_types_observable_types_get.sync(client=client)
print(types)
```

Every endpoint module under `aceapi_v2_client.api.*` exposes four functions:

| function          | returns                          |
| ----------------- | -------------------------------- |
| `sync(...)`       | the parsed body (or `None`)      |
| `sync_detailed(...)` | a `Response` with status + parsed body |
| `asyncio(...)`    | the parsed body, async           |
| `asyncio_detailed(...)` | a `Response`, async         |

All take `client=` as a keyword argument plus any path/query/body parameters
the operation defines.

### Searching alerts

`POST /search/alerts` takes ACE's alert query language — free text plus any
number of `field:value` terms:

```python
from aceapi_v2_client.api.search import search_alerts_search_alerts_post
from aceapi_v2_client.models import AlertSearchRequest

results = search_alerts_search_alerts_post.sync(
    client=client,
    body=AlertSearchRequest(query="disposition:DELIVERY alert_date:-7d"),
)
print(results.total)
for result in results.results:
    # each result wraps the alert summary plus its ranking metadata
    print(result.rank, result.score, result.alert.uuid, result.alert.description)
```

Terms may be inverted with a leading `-`, ORed by separating values with commas,
and quoted when a value contains a space. `detection_point:<signature uuid>[:<version>]`
narrows to alerts with a detection point from that signature; the same filter is
available structurally as `SearchFiltersBody(detection_points=[...])`.
`POST /search/similar` takes an alert UUID instead and returns the alerts nearest
to it.

### Async usage

```python
import asyncio
from aceapi_v2_client.auth import authenticated_client
from aceapi_v2_client.api.common import ping_common_ping_get

client = authenticated_client("https://localhost:8443/api/v2", "YOUR-API-KEY",
                              verify_ssl=False)

async def main():
    async with client as c:
        print(await ping_common_ping_get.asyncio(client=c))

asyncio.run(main())
```

## API keys are scoped

An API key carries its own permission scope. A key's **effective permission is
the intersection of that scope with its owner's permissions** — a key can never
do more than its owner, and a restricted key does strictly less. A key created
with "inherit" scope simply gets whatever its owner has.

The practical consequence for client code: a call can fail with
`403 {"detail": "Permission denied"}` even though the key is valid and the owner
is privileged, because the *key* is scoped too narrowly. Most read/write
endpoints are permission-gated — including `/observable-types/`, the
`observable-*`, `threat*`, `search`, `alerts`, `crashes` and `signatures/yara-qa`
endpoints (`signature:read`; the yara-qa downloads need `signature:download`), and
`/common/valid_*`, as well as the alert listing (`alert:read`), remediation
(`remediation:read` / `remediation:write`), file collection
(`file_collection:read`), CLI (`cli:execute`) and `svs` endpoints (`svs:run_read`,
`svs:run_manage`, `svs:admin`, and `signature:read` / `signature:download` for the
samples). Only `/health/ping`, `/common/ping`,
`/common/supported_api_version`, and `/users/me/apikeys` are reachable with any
valid key.

**Self-service endpoints are the exception in the other direction.** `/users/me`,
`/users/me/preferences*` and the saved-filter endpoints act only on the caller's
own account and GUI state, so they check no permission at all — but they *do*
require a credential that carries no narrowing scope. An inherit-scoped key (or
the GUI's session cookie) passes; a key issued for one narrow machine task gets
`403 {"detail": "Permission denied"}` no matter how privileged its owner is.

Keys are **display-once**: the plaintext is returned only by the create call and
is never recoverable afterward. Mint one with `POST /users/{user_id}/apikeys`
(requires `user:write`) or from the CLI:

```bash
ace user add-api-key    # also: list-api-keys, revoke-api-key
```

To see your own keys — metadata only, never the secret:

```python
from aceapi_v2_client.api.users import list_my_api_keys_users_me_apikeys_get

for key in list_my_api_keys_users_me_apikeys_get.sync(client=client):
    print(key.id, key.name, key.inherit_user_scope, key.scope)
```

> JWT/OAuth2 login (`POST /auth/token`, `POST /auth/refresh`) and the
> `token_client` helper were removed. The API key above is the only mechanism
> available to a machine client.

## Endpoint coverage

The client covers **every endpoint the API publishes** — all 256 operations
across the groups below. `tests/test_coverage.py` enforces this: it reads the
vendored `openapi.json`, imports the matching module for each operation, and
fails if the API grew an endpoint the client has not been regenerated for (or
kept one the API dropped). It needs no running instance.

<details>
<summary><code>aceapi_v2_client.api.alerts</code> — 25 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /alerts/` | `list_alerts_alerts_get` |
| `POST /alerts/bulk-add-observable` | `bulk_add_observable_alerts_bulk_add_observable_post` |
| `GET /alerts/count` | `count_alerts_alerts_count_get` |
| `GET /alerts/date-range` | `resolve_date_range_alerts_date_range_get` |
| `GET /alerts/export/csv` | `export_alerts_csv_alerts_export_csv_get` |
| `GET /alerts/export/ndjson` | `export_alerts_ndjson_alerts_export_ndjson_get` |
| `PUT /alerts/owner` | `set_alert_owner_alerts_owner_put` |
| `GET /alerts/{alert_uuid}` | `get_alert_alerts_alert_uuid_get` |
| `PATCH /alerts/{alert_uuid}/comments/{comment_id}` | `update_alert_comment_alerts_alert_uuid_comments_comment_id_patch` |
| `GET /alerts/{alert_uuid}/detection-points` | `list_alert_detection_points_alerts_alert_uuid_detection_points_get` |
| `POST /alerts/{alert_uuid}/detection-points/confirm` | `confirm_detection_point_verdicts_alerts_alert_uuid_detection_points_confirm_post` |
| `DELETE /alerts/{alert_uuid}/detection-points/{content_hash}/verdict` | `clear_detection_point_verdict_alerts_alert_uuid_detection_points_content_hash_verdict_delete` |
| `PUT /alerts/{alert_uuid}/detection-points/{content_hash}/verdict` | `set_detection_point_verdict_alerts_alert_uuid_detection_points_content_hash_verdict_put` |
| `GET /alerts/{alert_uuid}/download` | `download_alert_alerts_alert_uuid_download_get` |
| `GET /alerts/{alert_uuid}/logs` | `view_alert_logs_alerts_alert_uuid_logs_get` |
| `GET /alerts/{alert_uuid}/meta` | `get_alert_meta_alerts_alert_uuid_meta_get` |
| `POST /alerts/{alert_uuid}/observables/{observable_uuid}/check-for-clickers` | `check_for_clickers_alerts_alert_uuid_observables_observable_uuid_check_for_clickers_post` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/clicker-searches` | `get_clicker_searches_alerts_alert_uuid_observables_observable_uuid_clicker_searches_get` |
| `POST /alerts/{alert_uuid}/observables/{observable_uuid}/collect-file` | `collect_file_alerts_alert_uuid_observables_observable_uuid_collect_file_post` |
| `POST /alerts/{alert_uuid}/observables/{observable_uuid}/crawl` | `crawl_url_alerts_alert_uuid_observables_observable_uuid_crawl_post` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/hex` | `view_observable_file_as_hex_alerts_alert_uuid_observables_observable_uuid_hex_get` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/image` | `get_observable_image_alerts_alert_uuid_observables_observable_uuid_image_get` |
| `POST /alerts/{alert_uuid}/observables/{observable_uuid}/render` | `render_file_alerts_alert_uuid_observables_observable_uuid_render_post` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/text` | `view_observable_file_as_text_alerts_alert_uuid_observables_observable_uuid_text_get` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/zip` | `download_observable_file_alerts_alert_uuid_observables_observable_uuid_zip_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.analysis</code> — 1 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /analysis/` | `submit_analysis_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.cli</code> — 3 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /cli/executions` | `list_executions_cli_executions_get` |
| `POST /cli/executions` | `create_execution_cli_executions_post` |
| `GET /cli/executions/{execution_id}` | `get_execution_cli_executions_execution_id_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.common</code> — 5 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /common/ping` | `ping_common_ping_get` |
| `GET /common/supported_api_version` | `supported_api_version_common_supported_api_version_get` |
| `GET /common/valid_companies` | `valid_companies_common_valid_companies_get` |
| `GET /common/valid_directives` | `valid_directives_common_valid_directives_get` |
| `GET /common/valid_observables` | `valid_observables_common_valid_observables_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.crashes</code> — 3 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /crashes/` | `list_crash_reports_crashes_get` |
| `GET /crashes/{crash_id}` | `get_crash_report_crashes_crash_id_get` |
| `GET /crashes/{crash_id}/download` | `download_crash_report_crashes_crash_id_download_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.detection</code> — 5 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /detection/` | `list_detections_detection_get` |
| `POST /detection/` | `create_detection_detection_post` |
| `GET /detection/types` | `observable_types_detection_types_get` |
| `DELETE /detection/{detection_id}` | `delete_detection_detection_detection_id_delete` |
| `PATCH /detection/{detection_id}/expiration` | `set_expiration_detection_detection_id_expiration_patch` |

</details>

<details>
<summary><code>aceapi_v2_client.api.detection_points</code> — 3 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /detection-points/` | `list_detection_points_detection_points_get` |
| `GET /detection-points/export/csv` | `export_detection_points_csv_detection_points_export_csv_get` |
| `GET /detection-points/export/ndjson` | `export_detection_points_ndjson_detection_points_export_ndjson_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.email</code> — 1 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /email/archive` | `get_archived_email_email_archive_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.events</code> — 4 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /events/export` | `export_events_events_export_get` |
| `GET /events/open` | `open_events_events_open_get` |
| `PATCH /events/{event_id}` | `update_event_status_events_event_id_patch` |
| `GET /events/{event_ref}` | `get_event_events_event_ref_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.file_collections</code> — 7 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /file-collections/` | `list_file_collections_file_collections_get` |
| `GET /file-collections/export/csv` | `export_file_collections_csv_file_collections_export_csv_get` |
| `GET /file-collections/export/ndjson` | `export_file_collections_ndjson_file_collections_export_ndjson_get` |
| `DELETE /file-collections/{collection_id}` | `delete_file_collection_file_collections_collection_id_delete` |
| `POST /file-collections/{collection_id}/cancel` | `cancel_file_collection_file_collections_collection_id_cancel_post` |
| `GET /file-collections/{collection_id}/history` | `get_file_collection_history_file_collections_collection_id_history_get` |
| `POST /file-collections/{collection_id}/retry` | `retry_file_collection_file_collections_collection_id_retry_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.health</code> — 1 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /health/ping` | `ping_health_ping_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.hunt</code> — 1 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /hunt/validate` | `validate_hunt_hunt_validate_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.nodes</code> — 4 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /nodes/` | `list_nodes_nodes_get` |
| `GET /nodes/{node_id}` | `get_node_nodes_node_id_get` |
| `POST /nodes/{node_id}/drain` | `drain_node_nodes_node_id_drain_post` |
| `POST /nodes/{node_id}/resume` | `resume_node_nodes_node_id_resume_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.observables</code> — 7 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /observable-comments/` | `create_comment_observable_comments_post` |
| `DELETE /observable-comments/{comment_id}` | `delete_comment_observable_comments_comment_id_delete` |
| `PATCH /observable-comments/{comment_id}` | `update_comment_observable_comments_comment_id_patch` |
| `GET /observable-comments/{observable_id}` | `list_comments_observable_comments_observable_id_get` |
| `GET /observable-types/` | `list_observable_types_observable_types_get` |
| `PATCH /observables/interesting` | `set_interesting_observables_interesting_patch` |
| `POST /observables/lookup` | `lookup_observables_observables_lookup_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.remediation</code> — 10 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /remediation/remediations` | `list_remediations_remediation_remediations_get` |
| `POST /remediation/remediations` | `queue_remediations_remediation_remediations_post` |
| `GET /remediation/remediations/export/csv` | `export_remediations_csv_remediation_remediations_export_csv_get` |
| `GET /remediation/remediations/export/ndjson` | `export_remediations_ndjson_remediation_remediations_export_ndjson_get` |
| `DELETE /remediation/remediations/{remediation_id}` | `delete_remediation_remediation_remediations_remediation_id_delete` |
| `POST /remediation/remediations/{remediation_id}/cancel` | `cancel_remediation_remediation_remediations_remediation_id_cancel_post` |
| `GET /remediation/remediations/{remediation_id}/history` | `get_remediation_history_remediation_remediations_remediation_id_history_get` |
| `POST /remediation/remediations/{remediation_id}/restore` | `restore_remediation_remediation_remediations_remediation_id_restore_post` |
| `POST /remediation/remediations/{remediation_id}/retry` | `retry_remediation_remediation_remediations_remediation_id_retry_post` |
| `POST /remediation/targets/lookup` | `lookup_targets_remediation_targets_lookup_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.saved_filters</code> — 10 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /filter-screens/{screen}` | `get_filter_screen_descriptor_filter_screens_screen_get` |
| `GET /filter-screens/{screen}/decode` | `decode_filters_filter_screens_screen_decode_get` |
| `POST /filter-screens/{screen}/encode` | `encode_filters_filter_screens_screen_encode_post` |
| `GET /saved-filters/` | `list_saved_filters_saved_filters_get` |
| `POST /saved-filters/` | `create_saved_filter_saved_filters_post` |
| `PUT /saved-filters/quick-filters` | `set_quick_filters_saved_filters_quick_filters_put` |
| `PUT /saved-filters/scratch/{kind}` | `upsert_scratch_filter_saved_filters_scratch_kind_put` |
| `DELETE /saved-filters/{filter_uuid}` | `delete_saved_filter_saved_filters_filter_uuid_delete` |
| `GET /saved-filters/{filter_uuid}` | `get_saved_filter_saved_filters_filter_uuid_get` |
| `PATCH /saved-filters/{filter_uuid}` | `update_saved_filter_saved_filters_filter_uuid_patch` |

</details>

<details>
<summary><code>aceapi_v2_client.api.search</code> — 2 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /search/alerts` | `search_alerts_search_alerts_post` |
| `POST /search/similar` | `similar_alerts_search_similar_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.secrets</code> — 3 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /secrets/` | `list_secrets_secrets_get` |
| `DELETE /secrets/{key}` | `delete_secret_secrets_key_delete` |
| `PUT /secrets/{key}` | `set_secret_secrets_key_put` |

</details>

<details>
<summary><code>aceapi_v2_client.api.signatures</code> — 7 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /signatures/yara-qa/` | `list_signatures_signatures_yara_qa_get` |
| `GET /signatures/yara-qa/matches/{match_id}` | `get_match_signatures_yara_qa_matches_match_id_get` |
| `GET /signatures/yara-qa/matches/{match_id}/download` | `download_match_signatures_yara_qa_matches_match_id_download_get` |
| `GET /signatures/yara-qa/matches/{match_id}/record` | `get_match_record_signatures_yara_qa_matches_match_id_record_get` |
| `GET /signatures/yara-qa/{signature_uuid}` | `get_signature_signatures_yara_qa_signature_uuid_get` |
| `GET /signatures/yara-qa/{signature_uuid}/download` | `download_signature_matches_signatures_yara_qa_signature_uuid_download_get` |
| `GET /signatures/yara-qa/{signature_uuid}/matches` | `list_matches_signatures_yara_qa_signature_uuid_matches_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.svs</code> — 123 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /alerts/{alert_uuid}/svs` | `get_alert_svs_alerts_alert_uuid_svs_get` |
| `POST /alerts/{alert_uuid}/svs/disassociate` | `disassociate_alert_alerts_alert_uuid_svs_disassociate_post` |
| `POST /alerts/{alert_uuid}/svs/not-a-test` | `mark_not_a_test_alerts_alert_uuid_svs_not_a_test_post` |
| `GET /svs/catalog/repositories` | `list_repositories_svs_catalog_repositories_get` |
| `GET /svs/coverage/` | `list_coverage_svs_coverage_get` |
| `GET /svs/coverage/export/csv` | `export_coverage_csv_svs_coverage_export_csv_get` |
| `GET /svs/coverage/export/ndjson` | `export_coverage_ndjson_svs_coverage_export_ndjson_get` |
| `GET /svs/coverage/history` | `list_history_svs_coverage_history_get` |
| `GET /svs/coverage/history/counts` | `get_history_counts_svs_coverage_history_counts_get` |
| `GET /svs/coverage/history/export/csv` | `export_history_csv_svs_coverage_history_export_csv_get` |
| `GET /svs/coverage/history/export/ndjson` | `export_history_ndjson_svs_coverage_history_export_ndjson_get` |
| `GET /svs/coverage/summary` | `get_summary_svs_coverage_summary_get` |
| `GET /svs/coverage/{technique}` | `get_technique_svs_coverage_technique_get` |
| `GET /svs/expectations/` | `list_expectations_svs_expectations_get` |
| `GET /svs/expectations/export/csv` | `export_expectations_csv_svs_expectations_export_csv_get` |
| `GET /svs/expectations/export/ndjson` | `export_expectations_ndjson_svs_expectations_export_ndjson_get` |
| `GET /svs/ignores/` | `list_ignores_svs_ignores_get` |
| `GET /svs/ignores/export/csv` | `export_ignores_csv_svs_ignores_export_csv_get` |
| `GET /svs/ignores/export/ndjson` | `export_ignores_ndjson_svs_ignores_export_ndjson_get` |
| `DELETE /svs/ignores/global/{signature_uuid}` | `remove_global_ignore_svs_ignores_global_signature_uuid_delete` |
| `PUT /svs/ignores/global/{signature_uuid}` | `set_global_ignore_svs_ignores_global_signature_uuid_put` |
| `GET /svs/runs/` | `list_runs_svs_runs_get` |
| `POST /svs/runs/` | `register_run_svs_runs_post` |
| `GET /svs/runs/attributions` | `list_attributions_svs_runs_attributions_get` |
| `GET /svs/runs/attributions/export/csv` | `export_attributions_csv_svs_runs_attributions_export_csv_get` |
| `GET /svs/runs/attributions/export/ndjson` | `export_attributions_ndjson_svs_runs_attributions_export_ndjson_get` |
| `GET /svs/runs/batches` | `list_batches_svs_runs_batches_get` |
| `GET /svs/runs/batches/export/csv` | `export_batches_csv_svs_runs_batches_export_csv_get` |
| `GET /svs/runs/batches/export/ndjson` | `export_batches_ndjson_svs_runs_batches_export_ndjson_get` |
| `POST /svs/runs/bulk/cancel` | `cancel_runs_svs_runs_bulk_cancel_post` |
| `POST /svs/runs/bulk/close` | `close_runs_svs_runs_bulk_close_post` |
| `POST /svs/runs/bulk/end` | `end_runs_svs_runs_bulk_end_post` |
| `POST /svs/runs/bulk/take-ownership` | `take_ownership_svs_runs_bulk_take_ownership_post` |
| `GET /svs/runs/count` | `count_runs_svs_runs_count_get` |
| `GET /svs/runs/events` | `list_events_svs_runs_events_get` |
| `GET /svs/runs/events/export/csv` | `export_events_csv_svs_runs_events_export_csv_get` |
| `GET /svs/runs/events/export/ndjson` | `export_events_ndjson_svs_runs_events_export_ndjson_get` |
| `GET /svs/runs/export/csv` | `export_runs_csv_svs_runs_export_csv_get` |
| `GET /svs/runs/export/ndjson` | `export_runs_ndjson_svs_runs_export_ndjson_get` |
| `GET /svs/runs/results` | `list_results_svs_runs_results_get` |
| `GET /svs/runs/results/export/csv` | `export_results_csv_svs_runs_results_export_csv_get` |
| `GET /svs/runs/results/export/ndjson` | `export_results_ndjson_svs_runs_results_export_ndjson_get` |
| `GET /svs/runs/suppression-share` | `get_suppression_share_svs_runs_suppression_share_get` |
| `POST /svs/runs/validate` | `validate_registration_svs_runs_validate_post` |
| `GET /svs/runs/{run_id}` | `get_run_svs_runs_run_id_get` |
| `GET /svs/runs/{run_id}/alerts` | `list_run_alerts_svs_runs_run_id_alerts_get` |
| `GET /svs/runs/{run_id}/alerts/export/ndjson` | `export_run_alerts_ndjson_svs_runs_run_id_alerts_export_ndjson_get` |
| `POST /svs/runs/{run_id}/alerts/{alert_uuid}/associate` | `associate_alert_svs_runs_run_id_alerts_alert_uuid_associate_post` |
| `POST /svs/runs/{run_id}/alerts/{alert_uuid}/disassociate` | `disassociate_alert_svs_runs_run_id_alerts_alert_uuid_disassociate_post` |
| `POST /svs/runs/{run_id}/alerts/{alert_uuid}/keep` | `keep_context_svs_runs_run_id_alerts_alert_uuid_keep_post` |
| `POST /svs/runs/{run_id}/alerts/{alert_uuid}/not-a-test` | `mark_not_a_test_svs_runs_run_id_alerts_alert_uuid_not_a_test_post` |
| `GET /svs/runs/{run_id}/attributions` | `list_run_attributions_svs_runs_run_id_attributions_get` |
| `GET /svs/runs/{run_id}/attributions/export/csv` | `export_run_attributions_csv_svs_runs_run_id_attributions_export_csv_get` |
| `GET /svs/runs/{run_id}/attributions/export/ndjson` | `export_run_attributions_ndjson_svs_runs_run_id_attributions_export_ndjson_get` |
| `POST /svs/runs/{run_id}/cancel` | `cancel_run_svs_runs_run_id_cancel_post` |
| `POST /svs/runs/{run_id}/cleanup` | `run_cleanup_svs_runs_run_id_cleanup_post` |
| `GET /svs/runs/{run_id}/comments` | `list_run_comments_svs_runs_run_id_comments_get` |
| `POST /svs/runs/{run_id}/comments` | `add_run_comment_svs_runs_run_id_comments_post` |
| `DELETE /svs/runs/{run_id}/comments/{comment_id}` | `delete_run_comment_svs_runs_run_id_comments_comment_id_delete` |
| `PATCH /svs/runs/{run_id}/comments/{comment_id}` | `update_run_comment_svs_runs_run_id_comments_comment_id_patch` |
| `GET /svs/runs/{run_id}/events` | `list_run_events_svs_runs_run_id_events_get` |
| `GET /svs/runs/{run_id}/events/export/csv` | `export_run_events_csv_svs_runs_run_id_events_export_csv_get` |
| `GET /svs/runs/{run_id}/events/export/ndjson` | `export_run_events_ndjson_svs_runs_run_id_events_export_ndjson_get` |
| `POST /svs/runs/{run_id}/executed` | `run_executed_svs_runs_run_id_executed_post` |
| `GET /svs/runs/{run_id}/history` | `get_run_history_svs_runs_run_id_history_get` |
| `GET /svs/runs/{run_id}/results` | `list_run_results_svs_runs_run_id_results_get` |
| `GET /svs/runs/{run_id}/results/export/csv` | `export_run_results_csv_svs_runs_run_id_results_export_csv_get` |
| `GET /svs/runs/{run_id}/results/export/ndjson` | `export_run_results_ndjson_svs_runs_run_id_results_export_ndjson_get` |
| `POST /svs/runs/{run_id}/review` | `review_run_svs_runs_run_id_review_post` |
| `POST /svs/runs/{run_id}/start` | `start_run_svs_runs_run_id_start_post` |
| `GET /svs/samples/` | `list_samples_svs_samples_get` |
| `GET /svs/samples/captures/{capture_id}/record` | `get_capture_record_svs_samples_captures_capture_id_record_get` |
| `GET /svs/samples/deletions` | `list_deletions_svs_samples_deletions_get` |
| `GET /svs/samples/download` | `download_samples_svs_samples_download_get` |
| `GET /svs/samples/export/csv` | `export_samples_csv_svs_samples_export_csv_get` |
| `GET /svs/samples/export/ndjson` | `export_samples_ndjson_svs_samples_export_ndjson_get` |
| `GET /svs/samples/missing` | `list_missing_svs_samples_missing_get` |
| `DELETE /svs/samples/{sha256}` | `delete_sample_svs_samples_sha256_delete` |
| `GET /svs/samples/{sha256}/{rule_uuid}` | `get_sample_svs_samples_sha256_rule_uuid_get` |
| `POST /svs/samples/{sha256}/{rule_uuid}/confirm` | `confirm_sample_svs_samples_sha256_rule_uuid_confirm_post` |
| `GET /svs/samples/{sha256}/{rule_uuid}/download` | `download_sample_svs_samples_sha256_rule_uuid_download_get` |
| `DELETE /svs/samples/{sha256}/{rule_uuid}/label` | `reset_sample_label_svs_samples_sha256_rule_uuid_label_delete` |
| `PUT /svs/samples/{sha256}/{rule_uuid}/label` | `relabel_sample_svs_samples_sha256_rule_uuid_label_put` |
| `DELETE /svs/samples/{sha256}/{rule_uuid}/retirement` | `unretire_sample_svs_samples_sha256_rule_uuid_retirement_delete` |
| `PUT /svs/samples/{sha256}/{rule_uuid}/retirement` | `retire_sample_svs_samples_sha256_rule_uuid_retirement_put` |
| `GET /svs/test-hosts/` | `list_test_hosts_svs_test_hosts_get` |
| `POST /svs/test-hosts/` | `create_test_host_svs_test_hosts_post` |
| `GET /svs/test-hosts/export/csv` | `export_test_hosts_csv_svs_test_hosts_export_csv_get` |
| `GET /svs/test-hosts/export/ndjson` | `export_test_hosts_ndjson_svs_test_hosts_export_ndjson_get` |
| `DELETE /svs/test-hosts/{host_id}` | `delete_test_host_svs_test_hosts_host_id_delete` |
| `GET /svs/test-hosts/{host_id}` | `get_test_host_svs_test_hosts_host_id_get` |
| `PUT /svs/test-hosts/{host_id}` | `update_test_host_svs_test_hosts_host_id_put` |
| `DELETE /svs/test-hosts/{host}/maintenance` | `end_maintenance_svs_test_hosts_host_maintenance_delete` |
| `GET /svs/test-hosts/{host}/maintenance` | `list_maintenance_svs_test_hosts_host_maintenance_get` |
| `POST /svs/test-hosts/{host}/maintenance` | `open_maintenance_svs_test_hosts_host_maintenance_post` |
| `GET /svs/tests/` | `list_tests_svs_tests_get` |
| `GET /svs/tests/export/csv` | `export_tests_csv_svs_tests_export_csv_get` |
| `GET /svs/tests/export/ndjson` | `export_tests_ndjson_svs_tests_export_ndjson_get` |
| `GET /svs/tests/{guid}` | `get_test_svs_tests_guid_get` |
| `DELETE /svs/tests/{guid}/expectations/{platform}/{signature_uuid}` | `remove_expectation_svs_tests_guid_expectations_platform_signature_uuid_delete` |
| `PUT /svs/tests/{guid}/expectations/{platform}/{signature_uuid}` | `set_expectation_svs_tests_guid_expectations_platform_signature_uuid_put` |
| `DELETE /svs/tests/{guid}/ignores/{signature_uuid}` | `remove_test_ignore_svs_tests_guid_ignores_signature_uuid_delete` |
| `PUT /svs/tests/{guid}/ignores/{signature_uuid}` | `set_test_ignore_svs_tests_guid_ignores_signature_uuid_put` |
| `DELETE /svs/tests/{guid}/settings` | `remove_test_settings_svs_tests_guid_settings_delete` |
| `GET /svs/tests/{guid}/settings` | `get_test_settings_svs_tests_guid_settings_get` |
| `PUT /svs/tests/{guid}/settings` | `set_test_settings_svs_tests_guid_settings_put` |
| `GET /svs/worklist/` | `list_worklist_svs_worklist_get` |
| `POST /svs/worklist/bulk/resolve` | `bulk_resolve_svs_worklist_bulk_resolve_post` |
| `GET /svs/worklist/export/csv` | `export_worklist_csv_svs_worklist_export_csv_get` |
| `GET /svs/worklist/export/ndjson` | `export_worklist_ndjson_svs_worklist_export_ndjson_get` |
| `GET /svs/worklist/{signature_uuid}` | `get_signature_svs_worklist_signature_uuid_get` |
| `DELETE /svs/worklist/{signature_uuid}/{technique}/resolution` | `clear_resolution_svs_worklist_signature_uuid_technique_resolution_delete` |
| `PUT /svs/worklist/{signature_uuid}/{technique}/resolution` | `set_resolution_svs_worklist_signature_uuid_technique_resolution_put` |
| `GET /svs/yara/validations/` | `list_validations_svs_yara_validations_get` |
| `POST /svs/yara/validations/` | `request_validation_svs_yara_validations_post` |
| `GET /svs/yara/validations/export/csv` | `export_validations_csv_svs_yara_validations_export_csv_get` |
| `GET /svs/yara/validations/export/ndjson` | `export_validations_ndjson_svs_yara_validations_export_ndjson_get` |
| `GET /svs/yara/validations/{validation_uuid}` | `get_validation_svs_yara_validations_validation_uuid_get` |
| `GET /svs/yara/validations/{validation_uuid}/download` | `download_results_svs_yara_validations_validation_uuid_download_get` |
| `GET /svs/yara/validations/{validation_uuid}/results` | `list_results_svs_yara_validations_validation_uuid_results_get` |
| `GET /svs/yara/validations/{validation_uuid}/results/export/csv` | `export_results_csv_svs_yara_validations_validation_uuid_results_export_csv_get` |
| `GET /svs/yara/validations/{validation_uuid}/results/export/ndjson` | `export_results_ndjson_svs_yara_validations_validation_uuid_results_export_ndjson_get` |
| `GET /svs/yara/validations/{validation_uuid}/status` | `get_validation_status_svs_yara_validations_validation_uuid_status_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.threats</code> — 8 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /threat-types/` | `list_threat_types_threat_types_get` |
| `POST /threat-types/` | `create_threat_type_threat_types_post` |
| `DELETE /threat-types/{threat_type_id}` | `delete_threat_type_threat_types_threat_type_id_delete` |
| `GET /threat-types/{threat_type_id}` | `get_threat_type_threat_types_threat_type_id_get` |
| `PATCH /threat-types/{threat_type_id}` | `update_threat_type_threat_types_threat_type_id_patch` |
| `DELETE /threats/` | `delete_threat_threats_delete` |
| `GET /threats/` | `list_threats_threats_get` |
| `POST /threats/` | `create_threat_threats_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.users</code> — 23 operations</summary>

| operation | module |
| --------- | ------ |
| `PATCH /users/` | `update_users_users_patch` |
| `POST /users/` | `create_user_users_post` |
| `DELETE /users/apikeys/{key_id}` | `revoke_api_key_users_apikeys_key_id_delete` |
| `PUT /users/apikeys/{key_id}` | `update_api_key_users_apikeys_key_id_put` |
| `GET /users/catalog` | `permission_catalog_users_catalog_get` |
| `GET /users/details` | `user_details_users_details_get` |
| `POST /users/groups` | `create_group_users_groups_post` |
| `POST /users/groups/delete` | `delete_groups_users_groups_delete_post` |
| `GET /users/management-view` | `management_view_users_management_view_get` |
| `GET /users/me` | `get_me_users_me_get` |
| `PATCH /users/me` | `update_me_users_me_patch` |
| `GET /users/me/apikeys` | `list_my_api_keys_users_me_apikeys_get` |
| `POST /users/me/apikeys` | `create_my_api_key_users_me_apikeys_post` |
| `DELETE /users/me/apikeys/{key_id}` | `revoke_my_api_key_users_me_apikeys_key_id_delete` |
| `PUT /users/me/apikeys/{key_id}` | `update_my_api_key_users_me_apikeys_key_id_put` |
| `GET /users/me/preferences` | `get_preferences_users_me_preferences_get` |
| `DELETE /users/me/preferences/{key}` | `reset_preference_users_me_preferences_key_delete` |
| `GET /users/me/preferences/{key}` | `get_preference_users_me_preferences_key_get` |
| `PUT /users/me/preferences/{key}` | `set_preference_users_me_preferences_key_put` |
| `POST /users/permissions` | `add_permission_users_permissions_post` |
| `POST /users/permissions/delete` | `delete_permission_users_permissions_delete_post` |
| `GET /users/{user_id}/apikeys` | `list_user_api_keys_users_user_id_apikeys_get` |
| `POST /users/{user_id}/apikeys` | `create_api_key_users_user_id_apikeys_post` |

</details>

### Endpoints that do not return JSON

14 operations serve something other than `application/json`, besides the
list exports below. They still return their payload through `.parsed`, but with a
caveat on 10 of them:

| operation | `.parsed` holds | annotated as |
| --------- | --------------- | ------------ |
| `GET /alerts/{alert_uuid}/logs` | the log text | `str` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/hex` | a hex dump of the file | `str` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/text` | the file, as text | `str` |
| `GET /events/export` | the CSV export text | `str` |
| `GET /alerts/{alert_uuid}/download` | the zip, as **`bytes`** | `str` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/image` | the image, as **`bytes`** | `str` |
| `GET /alerts/{alert_uuid}/observables/{observable_uuid}/zip` | the zip, as **`bytes`** | `str` |
| `GET /crashes/{crash_id}/download` | the zip, as **`bytes`** | `str` |
| `GET /email/archive` | the raw email, as **`bytes`** | `str` |
| `GET /signatures/yara-qa/matches/{match_id}/download` | the zip, as **`bytes`** | `str` |
| `GET /signatures/yara-qa/{signature_uuid}/download` | the zip, as **`bytes`** | `str` |
| `GET /svs/samples/download` | the zip, as **`bytes`** | `str` |
| `GET /svs/samples/{sha256}/{rule_uuid}/download` | the zip, as **`bytes`** | `str` |
| `GET /svs/yara/validations/{validation_uuid}/download` | the zip, as **`bytes`** | `str` |

The 10 binary downloads really do hand back `bytes` at runtime — the `str`
annotation is an artifact of the schema declaring the body as a string with a
`contentMediaType`, and the generator honouring that literally. Write the result
straight to a file in binary mode:

```python
from pathlib import Path

from aceapi_v2_client.api.alerts import download_alert_alerts_alert_uuid_download_get

response = download_alert_alerts_alert_uuid_download_get.sync_detailed(
    alert_uuid="...", client=client
)
# .parsed and .content hold the same bytes; .content is the honestly-typed one
Path("alert.zip").write_bytes(response.content)
```

Every zip archive is **encrypted with the password `infected`**: they hold
files from an alert, a crash, a signature's matches or the SVS sample corpus,
which may be live malware.

Most list endpoints also have two streaming exports, `.../export/csv`
(22 operations) and `.../export/ndjson` (23). The CSV
exports parse into a `str`. The NDJSON exports return **`bytes`**, one JSON object
per line (again annotated `str`). Split and decode them yourself:

```python
import json

from aceapi_v2_client.api.alerts import export_alerts_ndjson_alerts_export_ndjson_get

body = export_alerts_ndjson_alerts_export_ndjson_get.sync(
    client=client, f=["alert_date:-7d"]
)
rows = [json.loads(line) for line in body.splitlines() if line]
```

A stream that fails part-way through cannot change the status code it already
sent, so it ends with an `{"error": ...}` line instead. Check the last row.

## Base URL and TLS notes

- **The base URL must include the `/api/v2` prefix.** The generated client
  appends operation paths (e.g. `/common/ping`) directly to `base_url`.
  - From inside the docker compose network: `https://ace-http/api/v2`
  - From the docker host: `https://localhost:8443/api/v2`
- Development instances serve a **self-signed certificate**. Pass
  `verify_ssl=False` (as above) or point `verify_ssl` at a CA bundle path for
  production.

## Keeping the client up to date

The generated code is committed to this repository. When the ACE API v2 changes,
regenerate it from the live schema:

```bash
# against the default instance (https://ace-http/api/v2/openapi.json)
scripts/regenerate.sh

# or against a specific instance
scripts/regenerate.sh https://localhost:8443/api/v2/openapi.json
```

The script:

1. fetches the latest `openapi.json` into this directory (the build-time source
   of truth),
2. drops the paths listed in `EXCLUDE_PATH_PREFIXES`, along with any component
   schema only they used. Today that is `/engine/*`: the node-to-node routes
   ACE's engines call on each other, which the API publishes in its schema but
   which are not for clients,
3. installs `openapi-python-client` into a throwaway virtualenv (so it never
   touches your main environment),
4. regenerates the package, preserving the hand-maintained files
   (`aceapi_v2_client/auth.py` and `aceapi_v2_client/py.typed`).

After running it:

1. **Check coverage**: `pytest tests/test_coverage.py` — this fails loudly if any
   endpoint in the new schema has no generated module. It runs offline.
2. **Review the diff**: `git diff aceapi_v2_client/`
3. **Bump the version** if the API changed — update `version` in
   `pyproject.toml` and `package_version_override` in
   `openapi-python-client-config.yaml`. The client version mirrors the API's
   major version (`2.x.y`); bump the patch/minor for client-only changes.
4. **Rebuild and verify** (below).

> Only `auth.py` and `py.typed` are hand-maintained. Do not add other custom
> code inside `aceapi_v2_client/` — it would be overwritten on regeneration.

### Watch the generator's warnings

The generator understands `application/json`, `application/octet-stream` and
`text/*` response bodies. Anything else makes it print a
`Cannot parse response ... Unsupported content_type` warning and **silently drop
that success response from the generated code** — `sync()` then returns `None` on
a perfectly good 200, and a client built with `raise_on_unexpected_status=True`
raises on it.

`openapi-python-client-config.yaml` already maps the API's `application/zip`,
`application/x-ndjson`, `message/rfc822` and `image/*` responses onto
`application/octet-stream` to avoid exactly that. If a
regeneration prints a new warning of this kind, add the content type to
`content_type_overrides` rather than shipping an endpoint that returns nothing.

> The regeneration script needs `python3 -m venv` to work. On Debian/Ubuntu,
> where `ensurepip` lives in a separate `python3-venv` package, it falls back to
> bootstrapping pip with `get-pip.py` — that path needs outbound network access
> to `bootstrap.pypa.io`.

## Building and publishing to PyPI

```bash
pip install -r requirements-dev.txt
python -m build              # produces dist/*.whl and dist/*.tar.gz
twine check dist/*           # validate metadata for PyPI
twine upload dist/*          # publish (requires PyPI credentials)
```

## Running the tests

`tests/test_coverage.py` runs offline — it checks the committed package against
the committed schema and needs nothing but the package's own dependencies:

```bash
pytest tests/test_coverage.py -v
```

`tests/test_smoke.py` only runs when pointed at a live instance, and is skipped
otherwise. It exercises one endpoint from each major group, including a
create/read/update/delete round trip against `/saved-filters/` that cleans up
after itself:

```bash
ACE_API_BASE_URL=https://ace-http/api/v2 \
ACE_API_KEY=YOUR-API-KEY \
ACE_API_VERIFY_SSL=false \
pytest tests/test_smoke.py -v
```

Point it at a key with an **inherit** scope: the `/users/me` and saved-filter
tests are self-service routes, which a narrowly scoped key cannot reach (see
[API keys are scoped](#api-keys-are-scoped)).

## License

Apache-2.0. See [LICENSE](LICENSE).
