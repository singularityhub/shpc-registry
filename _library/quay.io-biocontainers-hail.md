---
layout: container
name:  "quay.io/biocontainers/hail"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hail/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hail/container.yaml"
updated_at: "2025-02-21 03:30:53.131472"
latest: "0.2.61--py36hf1ae8f4_1"
container_url: "https://biocontainers.pro/tools/hail"
aliases:
 - "beeline"
 - "beeline.cmd"
 - "bq"
 - "docker-credential-gcloud"
 - "docker-image-tool.sh"
 - "find-spark-home"
 - "find-spark-home.cmd"
 - "find_spark_home.py"
 - "gcloud"
 - "hailctl"
 - "load-spark-env.cmd"
 - "load-spark-env.sh"
 - "pyspark"
 - "pyspark.cmd"
 - "pyspark2.cmd"
 - "run-example"
 - "run-example.cmd"
 - "spark-class"
 - "spark-class.cmd"
 - "spark-class2.cmd"
 - "spark-shell"
 - "spark-shell.cmd"
 - "spark-shell2.cmd"
 - "spark-sql"
 - "spark-sql.cmd"
 - "spark-sql2.cmd"
 - "spark-submit"
 - "spark-submit.cmd"
 - "spark-submit2.cmd"
 - "sparkR"
 - "sparkR.cmd"
 - "sparkR2.cmd"
 - "gsutil"
 - "google-oauthlib-tool"
 - "clhsdb"
 - "hsdb"
 - "get_objgraph"
 - "undill"
 - "bokeh"
 - "tabulate"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
versions:
 - "0.2.61--py36hf1ae8f4_1"
 - "0.2.61--py37h9a982cc_1"
description: "shpc-registry automated BioContainers addition for hail"
config: {"url": "https://biocontainers.pro/tools/hail", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hail", "latest": {"0.2.61--py36hf1ae8f4_1": "sha256:e95626893f2d3a582ed0b9681889822e4963b937ef50548706dcd2f0f60d2a88"}, "tags": {"0.2.61--py36hf1ae8f4_1": "sha256:e95626893f2d3a582ed0b9681889822e4963b937ef50548706dcd2f0f60d2a88", "0.2.61--py37h9a982cc_1": "sha256:a87929a0a07cf7680e2cc953a29dad2ac0821ebba83335e37add59f349c74c9c"}, "docker": "quay.io/biocontainers/hail", "aliases": {"beeline": "/usr/local/bin/beeline", "beeline.cmd": "/usr/local/bin/beeline.cmd", "bq": "/usr/local/bin/bq", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "docker-image-tool.sh": "/usr/local/bin/docker-image-tool.sh", "find-spark-home": "/usr/local/bin/find-spark-home", "find-spark-home.cmd": "/usr/local/bin/find-spark-home.cmd", "find_spark_home.py": "/usr/local/bin/find_spark_home.py", "gcloud": "/usr/local/bin/gcloud", "hailctl": "/usr/local/bin/hailctl", "load-spark-env.cmd": "/usr/local/bin/load-spark-env.cmd", "load-spark-env.sh": "/usr/local/bin/load-spark-env.sh", "pyspark": "/usr/local/bin/pyspark", "pyspark.cmd": "/usr/local/bin/pyspark.cmd", "pyspark2.cmd": "/usr/local/bin/pyspark2.cmd", "run-example": "/usr/local/bin/run-example", "run-example.cmd": "/usr/local/bin/run-example.cmd", "spark-class": "/usr/local/bin/spark-class", "spark-class.cmd": "/usr/local/bin/spark-class.cmd", "spark-class2.cmd": "/usr/local/bin/spark-class2.cmd", "spark-shell": "/usr/local/bin/spark-shell", "spark-shell.cmd": "/usr/local/bin/spark-shell.cmd", "spark-shell2.cmd": "/usr/local/bin/spark-shell2.cmd", "spark-sql": "/usr/local/bin/spark-sql", "spark-sql.cmd": "/usr/local/bin/spark-sql.cmd", "spark-sql2.cmd": "/usr/local/bin/spark-sql2.cmd", "spark-submit": "/usr/local/bin/spark-submit", "spark-submit.cmd": "/usr/local/bin/spark-submit.cmd", "spark-submit2.cmd": "/usr/local/bin/spark-submit2.cmd", "sparkR": "/usr/local/bin/sparkR", "sparkR.cmd": "/usr/local/bin/sparkR.cmd", "sparkR2.cmd": "/usr/local/bin/sparkR2.cmd", "gsutil": "/usr/local/bin/gsutil", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "bokeh": "/usr/local/bin/bokeh", "tabulate": "/usr/local/bin/tabulate", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hail.
shpc-registry automated BioContainers addition for hail
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hail
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hail:0.2.61--py36hf1ae8f4_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hail/0.2.61--py36hf1ae8f4_1
$ module help quay.io/biocontainers/hail/0.2.61--py36hf1ae8f4_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hail-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hail-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hail-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hail-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hail-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hail-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beeline

```bash
$ singularity exec <container> /usr/local/bin/beeline
$ podman run --it --rm --entrypoint /usr/local/bin/beeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beeline.cmd

```bash
$ singularity exec <container> /usr/local/bin/beeline.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/beeline.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beeline.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bq

```bash
$ singularity exec <container> /usr/local/bin/bq
$ podman run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-credential-gcloud

```bash
$ singularity exec <container> /usr/local/bin/docker-credential-gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-image-tool.sh

```bash
$ singularity exec <container> /usr/local/bin/docker-image-tool.sh
$ podman run --it --rm --entrypoint /usr/local/bin/docker-image-tool.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-image-tool.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-spark-home

```bash
$ singularity exec <container> /usr/local/bin/find-spark-home
$ podman run --it --rm --entrypoint /usr/local/bin/find-spark-home   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-spark-home   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-spark-home.cmd

```bash
$ singularity exec <container> /usr/local/bin/find-spark-home.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/find-spark-home.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-spark-home.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_spark_home.py

```bash
$ singularity exec <container> /usr/local/bin/find_spark_home.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_spark_home.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_spark_home.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcloud

```bash
$ singularity exec <container> /usr/local/bin/gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hailctl

```bash
$ singularity exec <container> /usr/local/bin/hailctl
$ podman run --it --rm --entrypoint /usr/local/bin/hailctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hailctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### load-spark-env.cmd

```bash
$ singularity exec <container> /usr/local/bin/load-spark-env.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/load-spark-env.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/load-spark-env.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### load-spark-env.sh

```bash
$ singularity exec <container> /usr/local/bin/load-spark-env.sh
$ podman run --it --rm --entrypoint /usr/local/bin/load-spark-env.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/load-spark-env.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyspark

```bash
$ singularity exec <container> /usr/local/bin/pyspark
$ podman run --it --rm --entrypoint /usr/local/bin/pyspark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyspark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyspark.cmd

```bash
$ singularity exec <container> /usr/local/bin/pyspark.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/pyspark.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyspark.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyspark2.cmd

```bash
$ singularity exec <container> /usr/local/bin/pyspark2.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/pyspark2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyspark2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-example

```bash
$ singularity exec <container> /usr/local/bin/run-example
$ podman run --it --rm --entrypoint /usr/local/bin/run-example   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-example   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-example.cmd

```bash
$ singularity exec <container> /usr/local/bin/run-example.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/run-example.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-example.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-class

```bash
$ singularity exec <container> /usr/local/bin/spark-class
$ podman run --it --rm --entrypoint /usr/local/bin/spark-class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-class   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-class.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-class.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-class.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-class.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-class2.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-class2.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-class2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-class2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-shell

```bash
$ singularity exec <container> /usr/local/bin/spark-shell
$ podman run --it --rm --entrypoint /usr/local/bin/spark-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-shell.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-shell.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-shell.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-shell.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-shell2.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-shell2.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-shell2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-shell2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-sql

```bash
$ singularity exec <container> /usr/local/bin/spark-sql
$ podman run --it --rm --entrypoint /usr/local/bin/spark-sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-sql.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-sql.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-sql.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-sql.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-sql2.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-sql2.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-sql2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-sql2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-submit

```bash
$ singularity exec <container> /usr/local/bin/spark-submit
$ podman run --it --rm --entrypoint /usr/local/bin/spark-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-submit.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-submit.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-submit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-submit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spark-submit2.cmd

```bash
$ singularity exec <container> /usr/local/bin/spark-submit2.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/spark-submit2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spark-submit2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sparkR

```bash
$ singularity exec <container> /usr/local/bin/sparkR
$ podman run --it --rm --entrypoint /usr/local/bin/sparkR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparkR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sparkR.cmd

```bash
$ singularity exec <container> /usr/local/bin/sparkR.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/sparkR.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparkR.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sparkR2.cmd

```bash
$ singularity exec <container> /usr/local/bin/sparkR2.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/sparkR2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparkR2.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsutil

```bash
$ singularity exec <container> /usr/local/bin/gsutil
$ podman run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)