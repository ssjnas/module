import pandas as pd
exp_df=pd.read_csv('ER_expense_5paisa.csv')
exp_df.columns
exp_df['DISTRIBUTED_AMT'] = exp_df['DISTRIBUTED_AMT'].fillna(0)
table = pd.pivot_table(exp_df,index=['ACCOUNT_CODE_N','VENDOR_NAME','VENDOR_CODE'],values=['DISTRIBUTED_AMT'],aggfunc=sum)
table.reset_index(inplace=True)
table.shape
sub_table=table.groupby('ACCOUNT_CODE_N')['DISTRIBUTED_AMT'].sum()
sub_table=sub_table.to_frame()
sub_table.reset_index(inplace=True)
sub_table.rename(columns = {'DISTRIBUTED_AMT':'total'}, inplace = True)
left_df=pd.merge(table,sub_table,on="ACCOUNT_CODE_N",how="left")
def calculating_percentage(per):
    DISTRIBUTED_AMT=per[0]
    total_y=per[1]
    return (DISTRIBUTED_AMT/total_y)*100

    
left_df['percentage']=left_df[['DISTRIBUTED_AMT','total']].apply(calculating_percentage,axis=1)
def slab_20_30(slab):
    percentage=slab
    if (percentage>=20 and percentage<=30):
        return percentage 
    else:
        return "none"

left_df['20-30']=left_df['percentage'].apply(slab_20_30)
def slab_30_40(slab):
    percentage=slab
    if (percentage>30 and percentage<=40):
        return percentage 
    else:
        return "none"
left_df['30-40']=left_df['percentage'].apply(slab_30_40)
def slab_30_40(slab):
    percentage=slab
    if (percentage>30 and percentage<=40):
        return percentage 
    else:
        return "none"
left_df['30-40']=left_df['percentage'].apply(slab_30_40)
def slab_40_50(slab):
    percentage=slab
    if (percentage>40 and percentage<=50):
        return percentage 
    else:
        return "none"
left_df['40-50']=left_df['percentage'].apply(slab_40_50)
def slab_50_100(slab):
    percentage=slab
    if (percentage>50 and percentage<=200):
        return percentage 
    else:
        return "none"
left_df['50+']=left_df['percentage'].apply(slab_50_100)
left_df.to_csv("validation_8.results.csv")