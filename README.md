# PERSEUS_SPARK_frontend
>This work was led by [Di Jin](http://www-personal.umich.edu/~dijin/) under the supervision of [Christos Faloutsos](http://www.cs.cmu.edu/~christos/) and [Danai Koutra](http://web.eecs.umich.edu/~dkoutra/). The implementation is cooperated with and supported by Mr. [Jackie Zhang](https://github.com/ReactiveXYZ-Dev)

This repository contains all files used to deploy PERSEUS_HUB on the local machine. Please refer to the [paper](https://www.mdpi.com/2227-9709/4/3/22) for more details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Please make sure you have Python2 and pip installed in the machine. 
* Please make sure Redis is running on your local machine by running:

```
redis-server
```

You may check its status through
```
redis-cli ping
```

Refer to **Redis Quick Start** for more details (https://redis.io/topics/quickstart).

* See [Troubleshooting](#Troubleshooting) if you encountered any issues.

### Installing

To install PERSEUS_HUB on your local machine, just run the command as follows.

Say what the step will be

```
./install.sh
```

And then you should be able to access to the login page in your default browser. Create an account with any email you want, and you should be able to see the frontend page.

End with an example of getting some data out of the system or using it for a little demo

## DATA in the demo

The data used in the demo is store in "Data-Visualization-Website-local-installable⁩/⁨app⁩/data⁩/demo⁩". The database that supports the frontend has two components:
* The edge file
* The data file

The edge file ("edges.tsv") records the connectivity of the input graph with the format <src, dst, weight>. It was inserted into the database through "edges.sql".
The data files include "db.csv" and "display.csv". The former contains the numerical node features while the latter records its projection/approximated values.
Note that the three files, "edges.tsv", "db.csv" and "display.csv" are the output of PERSEUS_SPARK. One may replace these files with whatever input data you have, on the condition of rewriting the corresponding SQL files.



## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Redis](https://redis.io/) - In-memory data structure store, cache and message broker used.
* [Sqlite3](https://www.sqlite.org/index.html) - Database engine used


## Troubleshooting

* SQL config error on Mac OSX installation
Error message: 
```
OSError: mysql_config not found
...
Command "python setup.py egg_info" failed with error code 1 in ...
```
Refer to this [post](https://github.com/clips/pattern/issues/203)

* Dataset not found error when accessing to the website
Please make sure you have Redis running on your machine.


## Authors

* **Di Jin** - *Corresponding author*
* **Jackie Zhang** - *Website deployment*

See also the list of contributors in the [paper](https://www.mdpi.com/2227-9709/4/3/22) who participated in this project.


## Acknowledgments

Please kindly cite this work if you find it useful:
```
@inproceedings{jin2017perseus,
  title={PERSEUS-HUB: Interactive and collective exploration of large-scale graphs},
  author={Jin, Di and Leventidis, Aristotelis and Shen, Haoming and Zhang, Ruowang and Wu, Junyue and Koutra, Danai},
  booktitle={Informatics},
  volume={4},
  number={3},
  pages={22},
  year={2017},
  organization={Multidisciplinary Digital Publishing Institute}
}
```
For further technical details, please reach out to [Di Jin](http://www-personal.umich.edu/~dijin/).

