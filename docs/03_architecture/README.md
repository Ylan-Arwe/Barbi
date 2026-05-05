# 03 Architecture

**Purpose:** System, data, API, and repository-structure guidance for turning the blueprint into code without losing boundaries.

**Audience:** Backend, full-stack, platform, and integration contributors.

**How to use this folder:** Read this section before creating new packages, services, schemas, or route families, and whenever you are unsure where implementation belongs.

**Relation to the repository tree:** This section is the main bridge between the documentation spine and the placeholder code tree under `apps/` and `src/ai_recruiting_platform/`.

**Neighboring documents:**
- [01 Product](../01_product/README.md)
- [04 AI automation](../04_ai_automation/README.md)
- [06 Delivery operations](../06_delivery_operations/README.md)

## Assets in this folder

- [API design and webhooks](api_design_and_webhooks.md): Route philosophy, schema rules, and webhook expectations.
- [Code localization plan](code_localization_plan.md): Explicit mapping from workflow responsibilities to placeholder files.
- [Data model and domain objects](data_model_and_domain_objects.md): Domain aggregates, boundary rules, and privacy-sensitive object families.
- [Repository asset map](repository_asset_map.md): Top-level folder crosswalk for humans and agents.
- [System architecture](system_architecture.md): Runtime layers, control flow, and component separation.
- [Technology architecture](technology_architecture.md): Stack direction, dependency policy, and explicit undecided areas.

## Working rule for this section

Treat these documents as repository-native execution references. When implementation changes the meaning, ownership, or prerequisite order of the concepts here, update this section and the relevant package README or checklist entry in the same session.
