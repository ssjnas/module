import pandas as pd
exp_df=pd.read_excel("5paisa_6months.xlsx")
exp_df.columns
exp_df.drop(['CLAIM_NUMBER', 'CLAIM_REQUSTER',
       'CLAIM_REQUSTER_CODE',  'REQUESTOR_COMPANY',
       'BUSINESS',  'INVOICE_CURRENCY_CODE', 'EXCHANGE_RATE',
       'INVOICE_AMOUNT_CONVERTED', 'REQUEST_AMOUNT',
       'TDS_AMOUNT', 'SERVICE_TAX', 'GST_TAX', 'IGST_TAX',
       'GET_RCM__CGST_TAX_AMT', 'CGST_TAX', 'SGST_TAX', 'UTGST_TAX',
       'RCM__CGST', 'RCM__SGST', 'RCM__IGST', 'RCM__UTGST',
       'BILL_AMOUNT_BEFORE_TDS', 'FINAL_PAYABLE_AMOUNT', 'AMOUNT_PAID',
       'HOLD_REASON', 'BILL_NUMBER',  'CREATION_DATE', 'START_EXPENSE_DATE', 'END_EXPENSE_DATE',
       'MKRDT', 'STATUS_APPROVE_DATE', 'CHEQUE_NUMBER', 'PAYMENT_MODE',
       'IS_LAST_YEAR_CLAIM', 'BILL_FOR_MONTH', 'INVOICE_TYPE', 'PAYMENT_CITY',
       'PRINT_LOCATION', 'UTR_NUMBER', 'VENDOR_BANK_NAME',
       'VENDOR_ACCOUNT_NUMBER', 'VENDOR_PAY_TO_NAME', 'PAYMENT_DATE',
       'REQUSTER_LOCATION', 'FIRST_APPROVER', 'BRANCH_CODE',
       'CEP_INITITOR_CODE', 'CEP_INITITOR_NAME', 
       'APPROVER_CODE', 'APPROVER_NAME', 'APPROVER_REMARK', 'PO_NUMBERS',
       'GRN_NUMBERS', 'BATCH_NAME', 'VOUCHER_NUMBER', 'INVOICE_STATUS',
       'WF_STATUS', 'PAYMENT_STATUS', 'COMBINED_STATUS', 'LINE_NUMBER',
       'INVOICE_DIST_AMOUNT_CONVERTED', 'ACCOUNT', 'ENTITY_CODE',
       'ACCOUNT_CODE', 'BRANCH_CODE_N', 'DEPARTMENT_CODE', 'PRODUCT_CODE',
       'ENTITY', 'BRANCH', 'DEPARTMENT', 'PRODUCT',
       'CHANNEL', 'INTERCOMPANY', 'FUTURE_M', 'FUTURE_N'],axis=1,inplace=True)
pd.to_numeric(exp_df['VENDOR_CODE'], errors ='coerce')
pd.to_numeric(exp_df['DISTRIBUTED_AMT'], errors ='coerce')
pd.to_numeric(exp_df['INVOICE_ID'], errors ='coerce')
exp_df['INVOICE_NUM']=exp_df['INVOICE_NUM'].astype(str)
exp_df['DESCRIPTION_N']=exp_df['DESCRIPTION_N'].astype(str)
exp_df['CEP_INITIATOR_REMARK']=exp_df['CEP_INITIATOR_REMARK'].astype(str)

def line_type_item(line):
    if line=="ITEM":
        return "ITEM" 
exp_df['LINE_TYPE_NEW']=exp_df['LINE_TYPE'].apply(line_type_item)
def new_cep(cep):
    return cep.lower()
exp_df['CEP_INITIATOR_REMARK']=exp_df['CEP_INITIATOR_REMARK'].apply(new_cep)
def new_desc(des):
    return des.lower()
exp_df['DESCRIPTION_N']=exp_df['DESCRIPTION_N'].apply(new_desc)
exp_df[['START_DATE', 'END_DATE', 'BILL_DATE']] = exp_df[['START_DATE', 'END_DATE', 'BILL_DATE']].fillna('31-Jan-2040')
exp_df[['VENDOR_CODE','DISTRIBUTED_AMT','INVOICE_NUM','DESCRIPTION_N','CEP_INITIATOR_REMARK','INVOICE_ID']]=exp_df[['VENDOR_CODE','DISTRIBUTED_AMT','INVOICE_NUM','DESCRIPTION_N','CEP_INITIATOR_REMARK','INVOICE_ID']].fillna("9999999999")
count_df_1=exp_df.groupby(['VENDOR_CODE','DISTRIBUTED_AMT','BILL_DATE','START_DATE','END_DATE','INVOICE_NUM','LINE_TYPE_NEW',"VENDOR_SITE_NAME"])['INVOICE_ID'].nunique().reset_index(name="invoice_id_count_1")
def first_point(point):
    if (point==1):
        return "pass"
    elif (point>1):
        return "Duplicate" 
        
count_df_1['remark_1']=count_df_1['invoice_id_count_1'].apply(first_point)
count_df_1.to_csv("first_point.csv")
exp_df=pd.merge(exp_df,count_df_1,on=['VENDOR_CODE','DISTRIBUTED_AMT','BILL_DATE','START_DATE','END_DATE','INVOICE_NUM','LINE_TYPE_NEW',"VENDOR_SITE_NAME"],how="left")
count_df_2=exp_df.groupby(['VENDOR_CODE','DISTRIBUTED_AMT','DESCRIPTION_N','BILL_DATE','START_DATE',"END_DATE","LINE_TYPE_NEW","VENDOR_SITE_NAME"])['INVOICE_ID'].nunique().reset_index(name="invoice_id_count_2")
def second_point(point):
    if (point==1):
        return "pass"
    elif (point>1):
        return "Duplicate"
count_df_2['remark_2']=count_df_2['invoice_id_count_2'].apply(second_point)
exp_df=pd.merge(exp_df,count_df_2,on=['VENDOR_CODE','DISTRIBUTED_AMT','DESCRIPTION_N','BILL_DATE','START_DATE',"END_DATE","LINE_TYPE_NEW","VENDOR_SITE_NAME"],how="left")
count_df_2.to_csv("second_point.csv")
count_df_3=exp_df.groupby(['VENDOR_CODE','DISTRIBUTED_AMT','DESCRIPTION_N','START_DATE',"END_DATE","LINE_TYPE_NEW","VENDOR_SITE_NAME"])['INVOICE_ID'].nunique().reset_index(name="invoice_id_count_3")
def third_point(point):
    if (point==1):
        return "pass"
    elif (point>1):
        return "Duplicate"
count_df_3['remark_3']=count_df_3['invoice_id_count_3'].apply(third_point)
exp_df=pd.merge(exp_df,count_df_3,on=['VENDOR_CODE','DISTRIBUTED_AMT','DESCRIPTION_N','START_DATE',"END_DATE","LINE_TYPE_NEW","VENDOR_SITE_NAME"],how="left")
count_df_3.to_csv("third_point.csv")
count_df_4=exp_df.groupby(['VENDOR_CODE','DISTRIBUTED_AMT','CEP_INITIATOR_REMARK','START_DATE',"END_DATE","LINE_TYPE_NEW","VENDOR_SITE_NAME"])['INVOICE_ID'].nunique().reset_index(name="invoice_id_count_4")
def fourth_point(point):
    if (point==1):
        return "pass"
    elif (point>1):
        return "Duplicate"
count_df_4['remark_4']=count_df_4['invoice_id_count_4'].apply(fourth_point)
exp_df=pd.merge(exp_df,count_df_4,on=['VENDOR_CODE','DISTRIBUTED_AMT','CEP_INITIATOR_REMARK','START_DATE',"END_DATE","LINE_TYPE_NEW","VENDOR_SITE_NAME"],how="left")
count_df_4.to_csv("fourth_point.csv")
count_df_5=exp_df.groupby(['VENDOR_CODE','BILL_DATE','START_DATE',"END_DATE",'INVOICE_AMOUNT'])['INVOICE_ID'].nunique().reset_index(name="invoice_id_count_5")
def fifth_point(point):
    if (point==1):
        return "pass"
    elif (point>1):
        return "Duplicate"
count_df_5['remark_5']=count_df_5['invoice_id_count_5'].apply(fifth_point)
exp_df=pd.merge(exp_df,count_df_5,on=['VENDOR_CODE','BILL_DATE','START_DATE',"END_DATE",'INVOICE_AMOUNT'],how="left")
count_df_5.to_csv("fifth_point.csv")
count_df_6=exp_df.groupby(['VENDOR_CODE','BILL_DATE','INVOICE_AMOUNT'])['INVOICE_ID'].nunique().reset_index(name="invoice_id_count_6")
def sixth_point(point):
    if (point==1):
        return "pass"
    elif (point>1):
        return "Duplicate"
count_df_6['remark_6']=count_df_6['invoice_id_count_6'].apply(sixth_point)
exp_df=pd.merge(exp_df,count_df_6,on=['VENDOR_CODE','BILL_DATE','INVOICE_AMOUNT'],how="left")
exp_df.drop(['invoice_id_count_6','invoice_id_count_5','invoice_id_count_4','invoice_id_count_3','invoice_id_count_2','invoice_id_count_1'], axis=1,inplace=True)
exp_df[[ 'remark_5','remark_6']] = exp_df[[ 'remark_5','remark_6']].fillna('pass')
exp_df[['START_DATE', 'END_DATE', 'BILL_DATE']] = exp_df[['START_DATE', 'END_DATE', 'BILL_DATE']].replace("31-Jan-2040"," ")
exp_df[['VENDOR_CODE','DISTRIBUTED_AMT','INVOICE_NUM','DESCRIPTION_N','CEP_INITIATOR_REMARK','INVOICE_ID']]=exp_df[['VENDOR_CODE','DISTRIBUTED_AMT','INVOICE_NUM','DESCRIPTION_N','CEP_INITIATOR_REMARK','INVOICE_ID']].replace("9999999999","")
def remark_update(remark):
    remark_1=remark[0]
    LINE_TYPE=remark[1]
    if pd.isnull(remark_1):
        return LINE_TYPE 
    else:
        return remark_1
exp_df['remark_1']=exp_df[['remark_1','LINE_TYPE']].apply(remark_update,axis=1)
def validation_status_1(val):
    remark_1=val
    if remark_1=="Duplicate":
        return "fail"
    elif remark_1=="pass":
        return "pass"
    else:
        return "NA"
exp_df['Val_1']=exp_df['remark_1'].apply(validation_status_1)
def remark_update_2(remark):
    remark_2=remark[0]
    LINE_TYPE=remark[1]
    if pd.isnull(remark_2):
        return LINE_TYPE 
    else:
        return remark_2
exp_df['remark_2']=exp_df[['remark_2','LINE_TYPE']].apply(remark_update_2,axis=1)
def validation_status_2(val):
    remark_2=val
    if remark_2=="Duplicate":
        return "fail"
    elif remark_2=="pass":
        return "pass"
    else:
        return "NA"
exp_df['Val_2']=exp_df['remark_2'].apply(validation_status_2)
def remark_update_3(remark):
    remark_3=remark[0]
    LINE_TYPE=remark[1]
    if pd.isnull(remark_3):
        return LINE_TYPE 
    else:
        return remark_3
exp_df['remark_3']=exp_df[['remark_3','LINE_TYPE']].apply(remark_update_3,axis=1)
def validation_status_3(val):
    remark_3=val
    if remark_3=="Duplicate":
        return "fail"
    elif remark_3=="pass":
        return "pass"
    else:
        return "NA"
exp_df['Val_3']=exp_df['remark_3'].apply(validation_status_3)
def remark_update_4(remark):
    remark_4=remark[0]
    LINE_TYPE=remark[1]
    if pd.isnull(remark_4):
        return LINE_TYPE 
    else:
        return remark_4
exp_df['remark_4']=exp_df[['remark_4','LINE_TYPE']].apply(remark_update_4,axis=1)
def validation_status_4(val):
    remark_4=val
    if remark_4=="Duplicate":
        return "fail"
    elif remark_4=="pass":
        return "pass"
    else:
        return "NA"
exp_df['Val_4']=exp_df['remark_4'].apply(validation_status_4)
def validation_status_5(val):
    if val=="Duplicate":
        return "fail"
    elif val=="pass":
        return "pass"
    else:
        return "blank"
exp_df['Val_5']=exp_df['remark_5'].apply(validation_status_5)
def validation_status_6(val):
    if val=="Duplicate":
        return "fail"
    elif val=="pass":
        return "pass"
    else:
        return "blank"
exp_df['Val_6']=exp_df['remark_6'].apply(validation_status_6)
exp_df=exp_df.sort_values(by=['VENDOR_CODE', 'DISTRIBUTED_AMT','INVOICE_NUM','END_DATE','START_DATE','BILL_DATE','LINE_TYPE_NEW',"VENDOR_SITE_NAME"],
               ascending=[True, True,True,True,True,True,True,True])
exp_df['Concatenate_1'] = exp_df['VENDOR_CODE'].astype(str) +" "+ exp_df['BILL_DATE'].astype(str)+" "+ exp_df['START_DATE'].astype(str)+" "+ exp_df['END_DATE'].astype(str)+" "+ exp_df['DISTRIBUTED_AMT'].astype(str)+" "+ exp_df['INVOICE_NUM'].astype(str)+" "+ exp_df['LINE_TYPE_NEW'].astype(str)+" "+exp_df['VENDOR_SITE_NAME'].astype(str)+" " +exp_df['Val_1'].astype(str)
exp_df['conc_num_1'] = exp_df.groupby('Concatenate_1').cumcount() + 1
exp_df['new_conc_num_1']=exp_df['conc_num_1'].shift(-1)
list_b=[1]
def rpaid_status_1(rpaid):
    conc_num_1=rpaid[0]
    Val_1=rpaid[1] 
    new_conc_num_1=rpaid[2]
    if (Val_1=="fail"):
        if (conc_num_1==1 and new_conc_num_1>1):
            count_inc=list_b[-1]+1
            list_b.append(count_inc)
            return list_b[-2]
        elif (conc_num_1>1):
            return list_b[-2]
exp_df['rpaid_1']=exp_df[['conc_num_1','Val_1','new_conc_num_1']].apply(rpaid_status_1,axis=1)
exp_df=exp_df.sort_values(by=['VENDOR_CODE', 'DISTRIBUTED_AMT','DESCRIPTION_N','END_DATE','START_DATE','BILL_DATE','LINE_TYPE_NEW',"VENDOR_SITE_NAME"],
               ascending=[True, True,True,True,True,True,True,True])
exp_df['Concatenate_2'] = exp_df['VENDOR_CODE'].astype(str) +" "+ exp_df['BILL_DATE'].astype(str)+" "+ exp_df['START_DATE'].astype(str)+" "+ exp_df['END_DATE'].astype(str)+" "+ exp_df['DISTRIBUTED_AMT'].astype(str)+" "+ exp_df['DESCRIPTION_N'].astype(str)+" "+ exp_df['LINE_TYPE_NEW'].astype(str)+" "+exp_df['VENDOR_SITE_NAME'].astype(str)+" "+exp_df['Val_2'].astype(str)
exp_df['conc_num_2'] = exp_df.groupby('Concatenate_2').cumcount() + 1
exp_df['new_conc_num_2']=exp_df['conc_num_2'].shift(-1)
list_c=[1]
def rpaid_status_2(rpaid):
    conc_num_2=rpaid[0]
    Val_2=rpaid[1] 
    new_conc_num_2=rpaid[2]
    if (Val_2=="fail"):
        if (conc_num_2==1 and new_conc_num_2>1):
            count_inc=list_c[-1]+1
            list_c.append(count_inc)
            return list_c[-2]
        elif (conc_num_2>1):
            return list_c[-2]
exp_df['rpaid_2']=exp_df[['conc_num_2','Val_2','new_conc_num_2']].apply(rpaid_status_2,axis=1)
exp_df=exp_df.sort_values(by=['VENDOR_CODE', 'DISTRIBUTED_AMT','DESCRIPTION_N','END_DATE','START_DATE','LINE_TYPE_NEW',"VENDOR_SITE_NAME"],
               ascending=[True, True,True,True,True,True,True])

exp_df['Concatenate_3'] = exp_df['VENDOR_CODE'].astype(str) +" "+ exp_df['START_DATE'].astype(str)+" "+ exp_df['END_DATE'].astype(str)+" "+ exp_df['DISTRIBUTED_AMT'].astype(str)+" "+ exp_df['DESCRIPTION_N'].astype(str)+" "+ exp_df['LINE_TYPE_NEW'].astype(str)+" "+exp_df['VENDOR_SITE_NAME'].astype(str)+" "+ exp_df['Val_3'].astype(str)
exp_df['conc_num_3'] =exp_df.groupby('Concatenate_3').cumcount() + 1
exp_df['new_conc_num_3']=exp_df['conc_num_3'].shift(-1)

list_d=[1]

def rpaid_status_3(rpaid):
    conc_num_3=rpaid[0]
    Val_3=rpaid[1] 
    new_conc_num_3=rpaid[2]
    if (Val_3=="fail"):
        if (conc_num_3==1 and new_conc_num_3>1):
            count_inc=list_d[-1]+1
            list_d.append(count_inc)
            return list_d[-2]
        elif (conc_num_3>1):
            return list_d[-2]

exp_df['rpaid_3']=exp_df[['conc_num_3','Val_3','new_conc_num_3']].apply(rpaid_status_3,axis=1)

exp_df=exp_df.sort_values(by=['VENDOR_CODE', 'DISTRIBUTED_AMT','CEP_INITIATOR_REMARK','END_DATE','START_DATE','LINE_TYPE_NEW',"VENDOR_SITE_NAME"],
               ascending=[True, True,True,True,True,True,True])

exp_df['Concatenate_4'] = exp_df['VENDOR_CODE'].astype(str) +" "+ exp_df['START_DATE'].astype(str)+" "+ exp_df['END_DATE'].astype(str)+" "+ exp_df['DISTRIBUTED_AMT'].astype(str)+" "+ exp_df['CEP_INITIATOR_REMARK'].astype(str)+" "+ exp_df['LINE_TYPE_NEW'].astype(str)+" "+exp_df['VENDOR_SITE_NAME'].astype(str)+" " + exp_df['Val_4'].astype(str)
exp_df['conc_num_4'] = exp_df.groupby('Concatenate_4').cumcount() + 1
exp_df['new_conc_num_4']=exp_df['conc_num_4'].shift(-1)

list_e=[1]

def rpaid_status_4(rpaid):
    conc_num_4=rpaid[0]
    Val_4=rpaid[1] 
    new_conc_num_4=rpaid[2]
    if (Val_4=="fail"):
        if (conc_num_4==1 and new_conc_num_4>1):
            count_inc=list_e[-1]+1
            list_e.append(count_inc)
            return list_e[-2]
        elif (conc_num_4>1):
            return list_e[-2]

exp_df['rpaid_4']=exp_df[['conc_num_4','Val_4','new_conc_num_4']].apply(rpaid_status_4,axis=1)

exp_df=exp_df.sort_values(by=['VENDOR_CODE', 'BILL_DATE','INVOICE_AMOUNT','END_DATE','START_DATE'],
               ascending=[True, True,True,True,True])

exp_df['Concatenate_5'] = exp_df['VENDOR_CODE'].astype(str) +" "+ exp_df['BILL_DATE'].astype(str)+" "+ exp_df['START_DATE'].astype(str)+" "+ exp_df['END_DATE'].astype(str)+" "+ exp_df['INVOICE_AMOUNT'].astype(str)+" "+ exp_df['Val_5'].astype(str)
exp_df['conc_num_5'] = exp_df.groupby('Concatenate_5').cumcount() + 1
exp_df['new_conc_num_5']=exp_df['conc_num_5'].shift(-1)

list_f=[1]

def rpaid_status_5(rpaid):
    conc_num_5=rpaid[0]
    Val_5=rpaid[1] 
    new_conc_num_5=rpaid[2]
    if (Val_5=="fail"):
        if (conc_num_5==1 and new_conc_num_5>1):
            count_inc=list_f[-1]+1
            list_f.append(count_inc)
            return list_f[-2]
        elif (conc_num_5>1):
            return list_f[-2]

exp_df['rpaid_5']=exp_df[['conc_num_5','Val_5','new_conc_num_5']].apply(rpaid_status_5,axis=1)

exp_df=exp_df.sort_values(by=['VENDOR_CODE', 'BILL_DATE','INVOICE_AMOUNT'],
               ascending=[True, True,True])

exp_df['Concatenate_6'] = exp_df['VENDOR_CODE'].astype(str) +" "+ exp_df['BILL_DATE'].astype(str)+" "+ exp_df['INVOICE_AMOUNT'].astype(str)+" "+ exp_df['Val_6'].astype(str)
exp_df['conc_num_6'] = exp_df.groupby('Concatenate_6').cumcount() + 1
exp_df['new_conc_num_6']=exp_df['conc_num_6'].shift(-1)

list_g=[1]

def rpaid_status_6(rpaid):
    conc_num_6=rpaid[0]
    Val_6=rpaid[1] 
    new_conc_num_6=rpaid[2]
    if (Val_6=="fail"):
        if (conc_num_6==1 and new_conc_num_6>1):
            count_inc=list_g[-1]+1
            list_g.append(count_inc)
            return list_g[-2]
        elif (conc_num_6>1):
            return list_g[-2]

exp_df['rpaid_6']=exp_df[['conc_num_6','Val_6','new_conc_num_6']].apply(rpaid_status_6,axis=1)

exp_df.drop(['Concatenate_5','Concatenate_4','Concatenate_3',"Concatenate_2","Concatenate_1","Concatenate_6","conc_num_5","conc_num_4","conc_num_3","conc_num_2","conc_num_1","conc_num_6","new_conc_num_5","new_conc_num_4","new_conc_num_3","new_conc_num_2","new_conc_num_1","new_conc_num_6"], axis=1,inplace=True)

exp_df=exp_df.sort_values(by=['rpaid_1', 'rpaid_2','rpaid_3','rpaid_4','rpaid_5','rpaid_6'],
               ascending=[True, True,True,True,True,True])

exp_df.to_excel("5paisa_val_1_results.xlsx")