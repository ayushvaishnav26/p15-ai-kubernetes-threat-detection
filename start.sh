#!/bin/bash

python main.py &

streamlit run dashboard/app.py --server.address=0.0.0.0