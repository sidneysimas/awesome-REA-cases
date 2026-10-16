# Greenlight video API: query fields with AI, then probe actual validation with invalid values

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-16
Stage: Analysis test

Greenlight build log 5-6 describes integrating duration and aspect-ratio settings for an unnamed preview-stage video model. Official material was thin and external articles outdated. Claude tried more than a dozen field names over half a day, receiving only unknown-field errors. The author says one five-cent query to the platform's search-grounded AI revealed that duration and ratio belong in response_format, while task type belongs in video_config. It also identified five tasks—text-to-video, image-to-video, reference-image generation, editing and extension—and a three-to-ten-second range. This is observation of a black-box interface rather than merely generating example code.

The author then sent 99 seconds expecting rejection, but the request was accepted and generated a clip at a cost of one dollar. They added a local three-to-ten-second check before sending requests. A later generic Gemini answer incorrectly claimed both engines supported a feature; invalid-value tests contradicted it. Some engines reveal validation failure only when the background job is polled, so receipt of a request does not establish acceptance of a parameter. The specific model, API version, currency clarification and complete requests/responses are not published, and the account says character names are pseudonyms. Field layouts, prices and ranges therefore remain claims about this integration, not a known vendor's API specification or evidence that all platform-hosted AI is reliable. REA is not evidenced, and no service calls were independently repeated here.

October 16 candidate snapshot: 0 likes, 264 views; half a day, five cents, one dollar and three-to-ten seconds are the author's account.

## Sources

- [Greenlight trilingual build log 5-6: fields and invalid-value probes](https://x.com/i/status/2110868326528303367)

[中文](../greenlight-video-api-field-probing.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
