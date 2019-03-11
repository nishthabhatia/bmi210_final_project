# bmi210_final_project

BMI210 Final Project: A Physical Fitness Recommendation Engine

To run this project, download this repository, and open up Terminal. Use the command `python .\app.py` to get started. Follow the prompts on screen to receive recommended and not recommended exercises.

## Introduction
Regular physical activity can dramatically improve one’s health. Understanding which exercises are tailored to an individual’s fitness goals and health injuries can help those individuals to establish sustainable, healthy exercising habits. According to a 2018 study by the CDC, less than 25% of Americans met national guidelines for physical activity in 2010-2015. This project aims to address this problem by developing an ontology-based advice system for exercise that individuals can utilize to enhance their fitness. 

## Methods
In order to accomplish our goals, we first construct an ontology in Protégé/OWL that encompasses exercises and their intended effects. The ontology is comprised of this, along with classes for eventual users of the system, and their corresponding goals and health data. Following this, we utilize Owlready2, a package for ontology-oriented programming in Python to construct our application. We implement two problem-solving classification methods in Python. Using our pre-constructed ontology as a base, we are able to instantiate and extend our ontology as a user interacts with our app, and complete our fitness recommendations for them with our functions.

## Evaluation
We will assess the impact and usefulness of our ontology and recommendation system by having a professional “grade” the results we provide for a given individual, based on the health data they input into the system. Aside from this, we will conduct a formative evaluation by asking subjectivist questions to potential users of our program, after they have tested out our program. 

## Conclusion
There currently exists no ontology that serves to categorize and represent physical fitness. The potential utility of an ontology and recommendation that links user goals and health data with potential remedies in fitness motivates the need for our project. Our application leverages this need, making it simple and easy for users to receive recommendations and non-recommendations for fitness activity that aligns with our newly constructed ontology.
