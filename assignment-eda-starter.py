import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Titanic App by Wanyin Yang')
df = pd.read_csv('train.csv')

# 显示数据集
st.write(df)

# 创建三个子图
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 绘制不同等级的箱图
for i, pclass in enumerate([1, 2, 3]):
    sns.boxplot(x='Pclass', y='Fare', data=df[df['Pclass'] == pclass], ax=axes[i], width=0.2)
    axes[i].set_xlabel(f'PClass={pclass}')
    axes[i].set_ylabel('')
    axes[i].set_xticks([0])
    axes[i].set_xticklabels(['Fare'])
    axes[i].grid(True)


plt.tight_layout()
st.pyplot(fig)
