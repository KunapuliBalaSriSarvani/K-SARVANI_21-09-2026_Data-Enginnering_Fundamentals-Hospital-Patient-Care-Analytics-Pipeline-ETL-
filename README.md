# 🏥 Hospital Patient Care Analytics Pipeline

> **End-to-End Data Engineering ETL Pipeline using Python, Pandas and MySQL**

## 📌 Project Overview

A multi-specialty hospital generates data from multiple operational systems such as **patient registration, appointments, laboratory reports, wearable devices, and doctor consultations**.

This project demonstrates an end-to-end **Data Engineering pipeline** that integrates these heterogeneous data sources, cleans and transforms the data, performs data-quality validation, and loads the processed dataset into **MySQL** for patient-care analytics.

The pipeline is designed to support analysis of:

- Patient waiting times
- Department-level operational performance
- Patient risk indicators
- Long-wait cases
- Healthcare-related analytical KPIs

---

## 🎯 Objectives

The main objectives of this project are:

1. **Integrate data from multiple hospital source systems**
2. **Clean and transform raw healthcare-related data**
3. **Calculate patient waiting-time metrics**
4. **Create analytical risk indicators from available patient attributes**
5. **Validate data quality before loading**
6. **Store the processed dataset in MySQL**
7. **Enable SQL-based analytics for patient-care insights**

---

# 🏗️ Data Engineering Architecture

```text
                    HOSPITAL SOURCE SYSTEMS
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Patient Data      Appointment Data    Laboratory Data
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    Vital / Wearable Data
                           │
                    Consultation Data
                           │
                           ▼
                    ┌─────────────┐
                    │   EXTRACT   │
                    │ Python/Pandas│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  TRANSFORM  │
                    │ Cleaning    │
                    │ Integration │
                    │ Feature Eng.│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  VALIDATE   │
                    │ Data Quality│
                    │   Checks    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    LOAD     │
                    │    MySQL    │
                    └──────┬──────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ PATIENT CARE        │
                 │ ANALYTICS           │
                 │                     │
                 │ SQL Queries / KPIs  │
                 └─────────────────────┘