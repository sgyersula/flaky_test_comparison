    public void testComplex(){
        List<EntityField> fieldList = FieldHelper.getFields(Admin.class);
        Assert.assertEquals(2, fieldList.size());
        Assert.assertEquals("admin", fieldList.get(0).getName());
        Assert.assertEquals("user", fieldList.get(1).getName());
    }
