import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

class Widgets:
    ''' This class is responsible for creating and populating all of the apps widgets''' 
    #
    # Whenever the class gets instantiated, meaning instances of the class get created, elements
    # defined inside the __init__ method upon instantiation get added to the class dictionary
    # and become part of the class attributes.
    def __init__(self, df, omit_columns=[]):
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.index.name = 'INDEX'
        df.reset_index(inplace=True)
        # A list containing data frame sections to be populated based on widget parameters.
        self.selections = []
        self.metric = ['Value Counts','Unique Items Count','Display Unique Items']
        self.state = st.session_state
        for column in omit_columns:
            if column in df.columns.tolist(): df = df.drop(column, axis=1)
            else:
                st.markdown(f'*Wrong column name **:blue[{column}]** ,verify spelling in **:green[omit_columns]** .*')
        self.DF = df
        self.start = self.assignment(df)
    #
    # This method assigns data types to data frame columns based on the columns majority  dtype.
    # It then sends each column into the create widget pipeline
    def assignment(self, df):
        for col in df.columns:
            try:
                majority_type = df[col].dropna().apply(type).value_counts().idxmax().__name__
                df[col] = df[col].astype(majority_type)
                data_type = df[col].dtype
                self.create_widget(df[col], data_type, col)
            except ValueError as ve:
                st.write(f'column type assignment error with the {col} column')
        return df 
    #
    # This method splits columns by their data types creating one of two types of widgets 
    def create_widget(self,df_col, data_type, col_name):
        elements = sorted(df_col.unique())
        widget_name = col_name.lower()
        if isinstance(data_type, (np.int64,
            int)) or data_type in ['int64'] and df_col.nunique() >= 3:
            mn, mx = int(df_col.min()), int(df_col.max())
            st.sidebar.slider(f"{col_name.title()}", mn, mx,(mn, mx), key=widget_name)
            widget_state = self.state[widget_name]
            self.filter(widget_state, widget_name, col_name, slide=True)
        else:
            st.sidebar.multiselect(f'{col_name.title()}', elements,key=widget_name)
            widget_state = self.state[widget_name]
            self.filter(widget_state, widget_name, col_name)
    # 
    # This method stores sections of the data frame dependent on each individual widgets modified parameters.
    # If the list is not empty, the new section before being added to the list, is verified by a conditional 
    # expression checking that it exists within the previous saved section in the list.
    def filter(self, state, widget_name, col_name, slide=False):
        if state:
            if self.selections:
                if len(self.selections) >= 2: del self.selections[0]
                idx = len(self.selections) - 1
                frame = self.selections[idx]
            if slide:
                if state[0] != self.DF[col_name].min() or state[1] != self.DF[col_name].max():
                    if self.selections:
                        mask = frame[(state[0] <= frame[col_name]) & (frame[col_name] <= state[1])]
                    else:
                        mask = self.DF[(state[0] <= self.DF[col_name]) & (self.DF[col_name] <= state[1])]
                    self.selections.append(mask)
            if self.selections and not slide:
                mask = frame[frame[col_name].isin(state)]
                self.selections.append(mask)
            else:
                if not slide:
                    mask = self.DF[self.DF[col_name].isin(state)]
                    self.selections.append(mask)
    #
    # This  is the method which is to be called by the user and ultimately returns the section of data
    # frame from the widget parameters or the data frame cropped to 12000 rows if it is larger.
    def show(self, msg=True):
        if self.selections:
            selected = self.selections[-1].iloc[0:12000] if len(self.selections[-1]) > 12000 else self.selections[-1]
        else:
            selected = self.DF if len(self.DF) < 12000 else self.DF.iloc[0:12000]
        length = selected.index.tolist()
        if len(selected) == 12000 and msg:
            st.markdown(f'*Big Data! **:blue[{len(self.DF)}]** rows, Display restricted to **:orange[12000]** rows , use the filters to see more*')
        if length and msg: st.markdown(f'Displaying row **:blue[{length[0]}]** to **:violet[{length[-1]}]**, **:orange[{len(length)}]** items')
        return selected
    #
    # A simple method which checks the length and selections sent from the metrics method.
    def check_len(self, option, column):
        if option == 'Unique Items Count':
            return st.markdown(f'**:violet[{self.DF[column].nunique()}]** Unique items in this column')
        elif option == 'Value Counts' or 'Display Unique Items':
            if len(self.DF.value_counts(self.DF[column])) > 12000:
                output = self.show().value_counts(self.show()[column]) if option == 'Value Counts' else self.show()[column].unique()
                return st.dataframe(output, use_container_width=True)
            else:
                output = self.DF.value_counts(self.DF[column]) if option == 'Value Counts' else self.DF[column].unique()
                return st.dataframe(output, use_container_width=True)
    #
    # Arguments from the metric_widgets method are sent to this method in order to build each
    # select box which allows the user to obtain specific column metrics
    def sub(self, index, column, normalize=False):
        index += 11
        st.selectbox('Choose metric', self.metric, key=str(index))
        if (option:=self.state[index]):
            return self.check_len(option, column)
    #
    # The method which generates the original select boxes inside of the expander widget.
    # This method send data to the sub method in order to build sub select boxes.
    def metric_widgets(self, normalize=False):
        cols = st.columns([3,3,3])
        state_name = 1
        for col in cols:
            with col:
                with st.expander('Metrics'):
                    st.selectbox('Column select', self.DF.columns.tolist(), key=str(state_name))
                    if (column:=self.state[str(state_name)]):
                        self.sub(state_name, column, normalize)
            state_name += 1
    #
    # The method needed for the user to gain access to the metric widgets.
    # This method is the catalyst which creates all sub widgets below the data frame.
    # It sends data to the metric_widgets method.
    def metrics(self, normalize=False):
        self.metric_widgets()
        with st.expander('Notes'):
            text = st.text_area('Notes in markdown or just notes', height=300)
            md = st.radio('Disable mark down', ('Enable','Disable'))
            if md == 'Enable': st.markdown(text)
