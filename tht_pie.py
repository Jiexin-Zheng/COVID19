import  datetime
import  json
from pyecharts import options as opts
from pyecharts.charts import Pie
#from pyecharts.faker import Faker
# 读原始数据文件
today = datetime.date.today().strftime('%Y%m%d')   #20200315
datafile = 'data/'+ today + '.json'
with open(datafile, 'r', encoding='UTF-8') as file:
    json_array = json.loads(file.read())

# 分析全国实时确诊数据：'confirmedCount'字段
china_data = []
for province in json_array:
    china_data.append((province['provinceShortName'], province['confirmedCount']))
china_data = sorted(china_data, key=lambda x: x[1], reverse=False)                 #reverse=True,表示降序，反之升序

x_data = [data[0] for data in china_data]
y_data = [data[1] for data in china_data]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])
c = (
    Pie()
    .add("", data_pair=data_pair)
#    .set_colors([])
    .set_global_opts(title_opts=opts.TitleOpts(title="COVID19"),legend_opts=opts.LegendOpts(is_show=False))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("COVID19.html")
)


