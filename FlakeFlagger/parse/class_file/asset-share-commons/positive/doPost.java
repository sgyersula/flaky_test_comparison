    public void doPost() throws ServletException, IOException {
        final byte[] expectedOutputStream = IOUtils.toByteArray(this.getClass().getResourceAsStream("AssetRenditionsDownloadServletTest__original.png"));
        doAnswer(invocation -> {
            Object[] args = invocation.getArguments();
            // Write some data to the response so we know that that requestDispatcher.include(..) was infact invoked.
            ((AssetRenditionDownloadResponse) args[1]).getOutputStream().write(expectedOutputStream);
            return null; // void method, return null
        }).when(requestDispatcher).include(any(SlingHttpServletRequest.class), any(SlingHttpServletResponse.class));

        ctx.registerInjectActivateService(new AssetRenditionsDownloadServlet());

        AssetRenditionsDownloadServlet servlet = (AssetRenditionsDownloadServlet) ctx.getService(Servlet.class);

        ctx.currentResource("/content/download-servlet");
        ctx.request().setMethod("POST");
        ctx.requestPathInfo().setResourcePath("/content/download-servlet");
        ctx.requestPathInfo().setSelectorString("asset-renditions-download");
        ctx.requestPathInfo().setExtension("zip");
        ctx.request().setQueryString("path=/content/dam/test.png&renditionName=test");

        servlet.service(ctx.request(), ctx.response());

        assertEquals("application/zip", ctx.response().getContentType());
        assertEquals(334,  ctx.response().getOutput().length);
    }
