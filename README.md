# Introduction:

Thanks for continuing your application to Postscript Engineering!

This assignment very closely mimics work we are doing at Postscript - it’s a stripped down version of a core part of our functionality. So it should give you a good sense of whether you want to work at Postscript, and give us a good sense of what it would be like to have you on our team. 

In particular, to do well on this project you’ll probably need to work like we do: follow the [80/20 rule](https://en.wikipedia.org/wiki/Pareto_principle). There are a lot of technologies listed below and we want you to use all of them. You’re probably not familiar with all of them, but you only need to learn enough to get the assignment working. We’re not looking for perfect usage of any tool.

In addition to the code, please send us: 1) an explanation of your solution, 2) a list of the technologies used that were totally new to you, so we can take that into account, 3) roughly how long you took

## Evaluation Criteria:

- Learning & implementing new frameworks / languages 
- Speed / Resourcefulness 
- Working within a broad spec / autonomous decision making
- Quality given the amount of time taken (it would be reasonable to submit a medium-quality solution that you were able to do quickly)

## Assignment:

Please create a tool that can send shipment notifications as text messages. All of the functionality you create must be exposed through a single front-end interface. It must interact with back-end API’s to perform its functions.

The main flows to implement are: 

- A user can choose a particular product and save a draft of a shipping notification for that product. For purposes of this assignment, we want to be able to create different shipping notifications for different products. There can be multiple draft message for a product or one per product, that is up to you.

- A user can also look up draft versions of these text messages that have been saved, and click a button to actually send one of them to a number (which they provide at the time of sending).

Additional details under “User Flows.”

## Tooling:

Please use the following technologies. If you are unfamiliar with them, learn the minimum required to get the job done. When you send in your assignment, you can tell us which ones you had to learn from scratch and we will take that into account.

- Flask (Python) to create the API endpoints
- Connect to DB using SQLAlchemy or pure SQL
- PostgreSQL database
- ReactJS Front-end (or Flask HTML)
- It is totally fine to use only pure HTML (via Flask) if you are unfamiliar with front-end technologies. There is room on our team for pure backend developers. But if you have front-end skills you can show them here.
- Twilio to send text messages (if for some reason you can’t create a trial account for free credit, let us know)

This does not need to be deployed and available to the internet as long as it can be run locally. The assignment should utilize Docker Compose in order to run locally on any setup.

## User Flows:

- Users should be able to query a list of available product_ids 
- Users should be able to create and save a message for a product
- Saving a message requires a product_id to be attached to the message and should throw an error otherwise
For example, the message object might look like 
```
{ 
  "message" : "Some string",
  "Product_id":1
}
  ```
- Users should be able to view messages for a product
- Users should be able to send messages for a product

- This should utilize the Twilio API -- use a Twilio trial account, it is OK if the message does not send to outside / non-whitelisted numbers.

## Getting Setup:

There are 2 folders contained with this homework:

**`api`**

The `api` folder houses the `Dockerfile` to build and run the `Flask` application against the `db`. It contains a bootstrapped `Flask` object and `Flask-SQLAlchemy` already setup to work with the larger `docker-compose.yml` file of this homework.

**`app`**

The `app` folder will house your frontend code and contains a `Dockerfile` that installs `package.json` with `npm` (or `yarn` if you uncomment it) and then executes `npm start` (or `yarn start`). The package.json does not currently exist (you will have to generate it with any packages you want) and the `docker-compose.yml` will startup the entire application folder when run. Be sure, whatever framework you use, you're able to start the frontend application on port 3000 or you'll need to update the `app/Dockerfile` and `docker-compose.yml` for your frontend port.

__Note:__ If you'd like to use `yarn` instead of `npm`, open the `app/Dockerfile` and swap `npm install --silent` with `yarn install --silent`

### Running the Environment

Once you've created a `package.json` in the `app` folder, you're ready to run the `docker-compose` environment.

By default, when running the `docker-compose` of this repo, the ports will map as follows:

- `api` - Port 5000
- `db` - Port 5432
- `app` - Port 3000

Running the environment is now as easy as `docker compose up`.

- Visit `http://localhost:5000/health-check` to verify the api is working.
- Visit `http://localhost:3000` to see your frontend application

## Delivery:

Please do not spend more than 5 hours on this assignment.

Please deliver the assignment in one of the following ways:

- Dropbox (sent to/shared with adam@postscript.io, madelyn@postscript.io, and patrick@postscript.io) 
- Google Drive (sent to/shared with adam@postscript.io, madelyn@postscript.io, and patrick@postscript.io) 
- Private Git Repo (shared with madelyneriksen, pkearney06, SpicyBajo) 

GH usernames (if private repo):
madelyneriksen
pkearney06
SpicyBajo




 
