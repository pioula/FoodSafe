## Motivation

We wanted to create a solution that will reduce the food waste, but will make life simpler at the same time. Some people might be disorganized while shopping, which might lead to extensive buying. Because of that it is possible that their fridge would be overloaded, thus some of the bought food might went into trash because of its expiration dates.

## Our solution

We designed a web site that acts as a smart fridge. Whenever you went back from shopping or used something you can update contents of it through a simple and intuitive UI. At any time, the user can request a personalized recipe, which is searched prioritizing usage of the contents of your fridge.

## How does it solve the problem?

Thanks to our recipe requesting system our users can be more efficient and planning shopping, thus buying only what they really need and refusing what they don't. Also, because of the prioritization of the fridge contents it is less likely that they will be expiring, thus reducing the food waste. Problem of managing food supplies affects everyone, so every people might be a user of our application.

## How can it be developed?

There are plenty of ways of developing this solution. Our main ideas are to make it more accessible to users and to be more successful at what it does:

> Scanning receipts - We could implement an OCR algorithm to include information about bought products from photos of the receipts. This have a potential of increasing the user experience.

> Auto managed fridge - We could include information about amount of products left for a certain type of product and implement algorithm that will reduce this amounts on selected recipe.

> Prioritization of products to their expiration date - to be even more sure that nothing would be wasted we could also include information about expiration date and implement the algorithm that will prioritize the products that are close the being expired.

## Our design

We have to micro services running on the k8s cluster in the google cloud. The first one is front end which delivers the user interface written in React. The second is backend written in Python Flask which communicates with frontend through HTTP methods and with firebase and spoonaccular API. We have also designed pipelines to push images of our services to k8s cluster automatically.

## How to run?
```sh
cd front && npm install && npm start
```
```sh
cd backend_products && pip install -r requirements.txt && python3 -m app.py
```