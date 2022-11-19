    public void test_for_issue() throws Exception {
        String json = "{\"create\":\"2018-01-10 08:30:00\"}";
        User user = JSON.parseObject(json, User.class);
        assertEquals("\"2018-01-10T08:30:00+08:00\"", JSON.toJSONString(user.create, SerializerFeature.UseISO8601DateFormat));
    }
