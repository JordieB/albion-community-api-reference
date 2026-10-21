"use strict";

const specUrl = new URL("openapi.yaml", window.location.href);
window.ui = SwaggerUIBundle({
  url: specUrl.href,
  dom_id: "#swagger-ui",
  deepLinking: true,
  filter: true,
  docExpansion: "none",
  defaultModelRendering: "model",
  supportedSubmitMethods: [],
  tryItOutEnabled: false,
  validatorUrl: null,
  queryConfigEnabled: false,
  persistAuthorization: false,
  requestInterceptor: (request) => {
    const target = new URL(request.url, window.location.href);
    if (target.href !== specUrl.href || (request.method || "GET").toUpperCase() !== "GET") {
      throw new Error("This reference loads its local OpenAPI document only.");
    }
    return request;
  }
});
