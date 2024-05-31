# novesHackathon

This repo was the challenge I faced on a 10-hours Hackathon, issued by <strong>Noves</strong>.

The challenge consisted of creating a transaction simulator of the blockchain, which has frontend-side and backend-side development.

This repo contain the backend side.

## USE CASE

I am going to explain the problem in order to understand the main idea of this repo. Let us suppose that you are navigating on the internet, and you receive a notification on your wallet. You can connect your wallet to the website you are on. And you just decide to connect it.
Here is a graphical representation of what is happening:

![image](https://github.com/pybalt/nevesHackathon/assets/96897286/68d78fd1-a683-4175-a704-5b2fc25fe778)

Here is where Noves comes to, and tries to present some solutions.

![image](https://github.com/pybalt/nevesHackathon/assets/96897286/77331685-dafc-4f11-a08c-2d027fc66d28)

So, in this case, we were working on the preview of the transactions.

So after reading some docs, 

https://docs.noves.fi/docs/wallets-learn-transaction-pre-sign

https://docs.noves.fi/reference/foresight-api-quickstart

and after seeing how simulators are implemented

https://docs.tenderly.co/simulations

https://www.alchemy.com/transaction-simulation

I think that the system may be something like this

![image](https://github.com/pybalt/nevesHackathon/assets/96897286/42f943b7-623a-487e-a9e9-dcd0314e522d)


## Instructions

You need docker to run this code. This single line is enough to have it working.

```bash
docker-compose build && docker-compose up
```

## Architecture

This backend only contains two modules, and there's another that I didn't have the time to develop. 

![image](https://github.com/pybalt/novesHackathon/assets/96897286/60f32b34-ec00-425c-a0e2-4b5f47e2e8b9)

