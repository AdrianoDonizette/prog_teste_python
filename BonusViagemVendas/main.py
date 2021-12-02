import pandas as pd
from twilio.rest import Client


account_sid ='ACb161f6ba6a89e8b15d5b7175fbc79f74'
auth_token = '534113a4919b09df67d17a149bee67cc'
client = Client(account_sid,auth_token)

lista_meses = ['janeiro','fevereiro','março','abril', 'maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if(tabela_vendas['Vendas']>55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']>55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']>55000,'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas} ')




message = client.messages.create(
     to ="+5521980809924",
    from_="+19704401546",
    body = f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
print(message.sid)



