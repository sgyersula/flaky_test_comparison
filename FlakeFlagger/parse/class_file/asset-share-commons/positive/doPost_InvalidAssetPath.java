    public void doPost_InvalidAssetPath() throws ServletException, IOException {
        ctx.registerInjectActivateService(new AssetRenditionsDownloadServlet());

        AssetRenditionsDownloadServlet servlet = (AssetRenditionsDownloadServlet) ctx.getService(Servlet.class);

        ctx.currentResource("/content/download-servlet");
        ctx.request().setMethod("POST");
        ctx.requestPathInfo().setResourcePath("/content/download-servlet");
        ctx.requestPathInfo().setSelectorString("asset-renditions-download");
        ctx.requestPathInfo().setExtension("zip");
        ctx.request().setQueryString("path=/content/dam/fake.png&renditionName=test");

        servlet.service(ctx.request(), ctx.response());

        assertEquals("application/zip", ctx.response().getContentType());
        assertEquals(253,  ctx.response().getOutput().length); // Size of zip w/ default no content message
    }
