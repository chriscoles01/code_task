


def main():
    pass




def get_next_faster(df, order, existing):
    top_series = order.index[0]

    df_top_series = df[df.index_x == top_series]
    df_top_series = df_top_series[df_top_series.index_y != top_series]

    matches = False
    set_existing_check =set(df_top_series[df.index_y.isin(existing)].constraint.tolist())

    if  set_existing_check== {1} or set_existing_check==set():
        existing.append(top_series)
        matches = True
        order = order.drop(top_series)

    return df, order,matches,existing

if __name__ == "__main__":
    pass