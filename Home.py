import streamlit as st
from hydralit import HydraHeadApp
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'

class HomeAPP(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):#-------------------existing untouched code------------------------------------------

        col1,col2,col3 =st.columns((1,15,1))
        with col2:
            st.markdown("# Introduction")

            st.markdown("#### XX is an integrated scRNA-seq database exclusively"
                        " dedicated to nasal studies，which is an accessible"
                        " supportive tool to analyze nose-associated single-cell"
                        " RNA sequencing data，and which encompasses 21 datasets"
                        " involving primarily epithelial and immune cell types, allowing"
                        " researchers to maximally use this data to provide new"
                        " insights into biomedicine.")


        col4,col5,col6,col7,col8 =st.columns((1,3,1,3,1))

        with col5:
            st.image("compenent0.png")

        with col7:
            st.markdown(
                """
                <div class="my-link">
                  <a href="Nasal_Cavity_Dataset">
                    <div class="my-container">
                      <img src="https://i.postimg.cc/Y2y95DNm/compenent2.png" alt="Image">
                      <div class="my-text">
                        <h3>Nasal Cavity&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</h3>
                        <p>EGA(3)&nbsp&nbsp&nbsp&nbspGEO(10)</p>
                        <span class="my-caption">View data!</span>
                      </div>
                    </div>
                  </a>
                </div>

                <style>
                  .my-link {
                    display: inline-block;
                    margin: 10px;
                  }
                  .my-container {
                    position: relative;
                    display: flex;
                    align-items: center;
                    padding: 10px;
                    background-color: #f2f2f2;
                    border-radius: 5px;
                  }
                  .my-container img {
                    max-width: 100px;
                    margin-right: 10px;
                  }
                  .my-text {
                    display: flex;
                    flex-direction: column;
                  }
                  .my-text h3 {
                    margin: 0;
                    align-items: center;
                  }
                  .my-text p {
                    color :black;
                    margin: 0;
                    align-items: center;
                  }
                  .my-caption {
                    position: absolute;
                    top: 100%;
                    left: 50%;
                    transform: translate(-50%, 10px);
                    opacity: 0;
                    background-color: #333;
                    color: #fff;
                    padding: 5px;
                    border-radius: 5px;
                    font-size: 12px;
                    white-space: nowrap;
                    transition: opacity 0.2s, transform 0.2s;
                  }
                  .my-container:hover .my-caption {
                    opacity: 1;
                    transform: translate(-50%, 0);
                  }
                  .my-link a {
                    text-decoration: none;
                  }
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="my-link">
                  <a href="#1">
                    <div class="my-container">
                      <img src="https://i.postimg.cc/5twQ159W/compenent3.png" alt="Image">
                      <div class="my-text">
                        <h3>Nasopharynx&nbsp&nbsp&nbsp&nbsp&nbsp</h3>
                        <p>Single Cell Portal(1)<br>GEO(1)&nbsp&nbsp&nbspCNCB(1)</p>
                        <span class="my-caption">View data!</span>
                      </div>
                    </div>
                  </a>
                </div>

                <style>
                  .my-link {
                    display: inline-block;
                    margin: 10px;
                  }
                  .my-container {
                    position: relative;
                    display: flex;
                    align-items: center;
                    padding: 10px;
                    background-color: #f2f2f2;
                    border-radius: 5px;
                  }
                  .my-container img {
                    max-width: 100px;
                    margin-right: 10px;
                  }
                  .my-text {
                    display: flex;
                    flex-direction: column;
                  }
                  .my-text h3 {
                    margin: 0;
                  }
                  .my-text p {
                    color :black;
                    margin: 0;
                  }
                  .my-caption {
                    position: absolute;
                    top: 100%;
                    left: 50%;
                    transform: translate(-50%, 10px);
                    opacity: 0;
                    background-color: #333;
                    color: #fff;
                    padding: 5px;
                    border-radius: 5px;
                    font-size: 12px;
                    white-space: nowrap;
                    transition: opacity 0.2s, transform 0.2s;
                  }
                  .my-container:hover .my-caption {
                    opacity: 1;
                    transform: translate(-50%, 0);
                  }
                  .my-link a {
                    text-decoration: none;
                  }
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="my-link">
                  <a href="#1">
                    <div class="my-container">
                      <img src="https://i.postimg.cc/3NvVbyFF/component1.png" alt="Image" width=300>
                      <div class="my-text">
                        <h3>Paranasal Sinus</h3>
                        <p>GEO(3)&nbsp&nbsp&nbspdbGaP(1)&nbsp&nbsp&nbspCNCB(1)&nbsp</p>
                        <span class="my-caption">View data!</span>
                      </div>
                    </div>
                  </a>
                </div>

                <style>
                  .my-link {
                    display: inline-block;
                    margin: 20px;
                  }
                  .my-container {
                    position: relative;
                    display: flex;
                    align-items: center;
                    padding: 10px;
                    background-color: #f2f2f2;
                    border-radius: 5px;
                  }
                  .my-container img {
                    max-width: 100px;
                    margin-right: 10px;
                  }
                  .my-text {
                    display: flex;
                    flex-direction: column;
                  }
                  .my-text h3 {
                    margin: 0;
                  }
                  .my-text p {
                    color :black;
                    margin: 0;
                  }
                  .my-caption {
                    position: absolute;
                    top: 100%;
                    left: 50%;
                    transform: translate(-50%, 10px);
                    opacity: 0;
                    background-color: #333;
                    color: #fff;
                    padding: 5px;
                    border-radius: 5px;
                    font-size: 12px;
                    white-space: nowrap;
                    transition: opacity 0.2s, transform 0.2s;
                  }
                  .my-container:hover .my-caption {
                    opacity: 1;
                    transform: translate(-50%, 0);
                  }
                  .my-link a {
                    text-decoration: none;
                  }
                </style>
                """,
                unsafe_allow_html=True
            )

