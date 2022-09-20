import itertools
from bokeh.palettes import Dark2_5 as palette
from bokeh.transform import dodge


def char_ma_db_dash(temp_df, p, str_mutlindex, source, pivot_table_ma):
    temp_df = temp_df.replace({'Oś główna': 'default', 'Oś pomocnicza': 'secon_axis'})
    len_y_prime_positions = len(temp_df.loc[temp_df['oś'] == 'default'])
    len_y_second_positions = len(temp_df.loc[temp_df['oś'] == 'secon_axis'])
    colors_fin = []
    colors = itertools.cycle(palette)
    #  todo dorobic mechanim automatycznego doboru grubosci kolumn i przesuniecia w zaleznosci od ilosc argumentow
    list_tmp = [0, -0.16, 0.16, -0.32, 0.32, -0.48, 0.48, -0.64, 0.64, -0.8, 0.8, -0.96, 0.96]
    for m, color in zip(range(len(temp_df)), colors):
        colors_fin.append(color)
    j = 0
    count_of_y_prime = 0
    count_of_y_second = 0
    for i, row in temp_df.iterrows():
        if row['oś'] == 'default':
            position = list_tmp[count_of_y_prime]
            count_of_y_prime += 1
        else:
            position = list_tmp[count_of_y_second]
            count_of_y_second += 1
        if row['Opcje'] == 'Wykres Słupkowy':
            p.vbar(x=dodge(str_mutlindex, position,
                           range=p.x_range), top=row['Nazwa parametru'], source=source,
                   width=0.16, legend_label=row['Nazwa parametru'], y_range_name=row['oś'], color=colors_fin[j])
        elif row['Opcje'] == 'Wykres liniowy':
            p.line(pivot_table_ma.index.values, pivot_table_ma[f'''{row['Nazwa parametru']}'''], line_width=1,
                   y_range_name=row['oś'],
                   legend=row['Nazwa parametru'], color=colors_fin[j])
        j += 1

def char_options(p):
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    p.axis.minor_tick_line_color = None
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 'vertical'
    p.xaxis.subgroup_label_orientation = 'vertical'