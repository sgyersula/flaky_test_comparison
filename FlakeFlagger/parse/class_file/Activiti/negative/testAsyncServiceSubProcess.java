  public void testAsyncEndEvent() {  
    // start process 
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("asyncEndEvent");
    // now there should be one job in the database:
    assertEquals(1, managementService.createJobQuery().count());
    
    Object value = runtimeService.getVariable(processInstance.getId(), "variableSetInExecutionListener");
    assertNull(value);
    
    waitForJobExecutorToProcessAllJobs(2000L, 200L);
    
    // the job is done
    assertEquals(0, managementService.createJobQuery().count());
    
    assertProcessEnded(processInstance.getId());
    
    if (processEngineConfiguration.getHistoryLevel().isAtLeast(HistoryLevel.AUDIT)) {
      List<HistoricVariableInstance> variables = historyService.createHistoricVariableInstanceQuery().processInstanceId(processInstance.getId()).list();
      assertEquals(3, variables.size());
      
      Object historyValue = null;
      for (HistoricVariableInstance variable : variables) {
        if ("variableSetInExecutionListener".equals(variable.getVariableName())) {
          historyValue = variable.getValue();
        }
      }
      assertEquals("firstValue", historyValue);
    }
  }
