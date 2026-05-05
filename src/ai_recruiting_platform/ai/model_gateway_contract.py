"""
Purpose:
- Define the provider-agnostic gateway contract for text, embedding, classification, and ranking-support model calls.

Planned public functions, classes, endpoints, workers, or components:
- `ModelGateway`
- `CompletionRequest`
- `EmbeddingRequest`
- `ModelInvocationRecord`
- `invoke_model()`

Major collaborators and dependencies:
- `services/scoring_service.py`
- `services/explainability_service.py`
- `services/reply_classification_service.py`

Inputs, outputs, and boundaries:
- Inputs: prompt or message payloads, model selection, budget policy, safety context. Outputs: structured model responses plus invocation metadata. Boundary: business decisions stay outside the gateway.

Implementation sequencing notes:
- Implement before the first real model provider is attached.

Related docs and checklist references:
- `docs/04_ai_automation/ai_ml_design.md`
- `Final-Productization-Checklist.md`
"""
