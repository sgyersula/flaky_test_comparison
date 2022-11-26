    public void testUser(){
        List<EntityField> fieldList = FieldHelper.getFields(User.class);
        Assert.assertEquals(2, fieldList.size());
        Assert.assertEquals("id", fieldList.get(0).getName());
        Assert.assertEquals("name", fieldList.get(1).getName());
    }
