    public void test() {
        Class<?> entityClass = User.class;
        EntityHelper.initEntityNameMap(entityClass, config);
        StringBuilder sqlBuilder = new StringBuilder();
        sqlBuilder.append(SqlHelper.selectAllColumns(entityClass));
        final EntityTable entityTable = EntityHelper.getEntityTable(entityClass);
        sqlBuilder.append(SqlHelper.fromTable(entityClass, entityTable.getName()));
        sqlBuilder.append(SqlHelper.whereAllIfColumns(entityClass, config.isNotEmpty()));
        final String sql = sqlBuilder.toString();
        Assert.assertEquals("SELECT id,user_name,address,state  FROM user " +
                "<where>" +
                "<if test=\"id != null\"> AND id = #{id}</if>" +
                "<if test=\"userName != null\"> AND user_name = #{userName}</if>" +
                "<if test=\"address != null\"> AND address = #{address, typeHandler=tk.mybatis.mapper.mapperhelper.ComplexEntityTest.AddressHandler}</if>" +
                "<if test=\"state != null\"> AND state = #{state}</if></where>", sql);

        final ResultMap resultMap = entityTable.getResultMap(configuration);
        final List<ResultMapping> resultMappings = resultMap.getResultMappings();
        final ResultMapping idMapping = resultMappings.get(0);
        final ResultMapping userNameMapping = resultMappings.get(1);
        final ResultMapping addressMapping = resultMappings.get(2);
        final ResultMapping stateMapping = resultMappings.get(3);

        Assert.assertEquals("id", idMapping.getColumn());
        Assert.assertEquals("id", idMapping.getProperty());
        Assert.assertTrue(idMapping.getFlags().contains(ResultFlag.ID));

        Assert.assertEquals("user_name", userNameMapping.getColumn());
        Assert.assertEquals("userName", userNameMapping.getProperty());

        Assert.assertEquals("address", addressMapping.getColumn());
        Assert.assertEquals("address", addressMapping.getProperty());
        Assert.assertEquals(AddressHandler.class, addressMapping.getTypeHandler().getClass());

        Assert.assertEquals("state", stateMapping.getColumn());
        Assert.assertEquals("state", stateMapping.getProperty());
        Assert.assertEquals(EnumTypeHandler.class, stateMapping.getTypeHandler().getClass());


    }
