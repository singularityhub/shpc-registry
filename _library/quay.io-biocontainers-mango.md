---
layout: container
name:  "quay.io/biocontainers/mango"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mango/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mango/container.yaml"
updated_at: "2024-08-26 02:48:48.080040"
latest: "0.0.5--pyh864c0ab_4"
container_url: "https://biocontainers.pro/tools/mango"
aliases:
 - "adam-shell"
 - "adam-submit"
 - "adamR"
 - "beeline"
 - "beeline.cmd"
 - "docker-image-tool.sh"
 - "find-adam-assembly.sh"
 - "find-adam-egg.sh"
 - "find-adam-home"
 - "find-mango-assembly.sh"
 - "find-mango-home"
 - "find-spark-home"
 - "find-spark-home.cmd"
 - "find-spark.sh"
 - "find_adam_home.py"
 - "find_spark_home.py"
 - "load-spark-env.cmd"
 - "load-spark-env.sh"
 - "make_genome"
 - "mango-notebook"
 - "mango-submit"
 - "pyadam"
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
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-notebook"
 - "jupyter-serverextension"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "jupyter-nbconvert"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
versions:
 - "0.0.5--pyh864c0ab_4"
description: "shpc-registry automated BioContainers addition for mango"
config: {"url": "https://biocontainers.pro/tools/mango", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mango", "latest": {"0.0.5--pyh864c0ab_4": "sha256:07103f9c7ba46c7940306ccf1b72f4bc3022fdd2186702d12c48994a0bd7945d"}, "tags": {"0.0.5--pyh864c0ab_4": "sha256:07103f9c7ba46c7940306ccf1b72f4bc3022fdd2186702d12c48994a0bd7945d"}, "docker": "quay.io/biocontainers/mango", "aliases": {"adam-shell": "/usr/local/bin/adam-shell", "adam-submit": "/usr/local/bin/adam-submit", "adamR": "/usr/local/bin/adamR", "beeline": "/usr/local/bin/beeline", "beeline.cmd": "/usr/local/bin/beeline.cmd", "docker-image-tool.sh": "/usr/local/bin/docker-image-tool.sh", "find-adam-assembly.sh": "/usr/local/bin/find-adam-assembly.sh", "find-adam-egg.sh": "/usr/local/bin/find-adam-egg.sh", "find-adam-home": "/usr/local/bin/find-adam-home", "find-mango-assembly.sh": "/usr/local/bin/find-mango-assembly.sh", "find-mango-home": "/usr/local/bin/find-mango-home", "find-spark-home": "/usr/local/bin/find-spark-home", "find-spark-home.cmd": "/usr/local/bin/find-spark-home.cmd", "find-spark.sh": "/usr/local/bin/find-spark.sh", "find_adam_home.py": "/usr/local/bin/find_adam_home.py", "find_spark_home.py": "/usr/local/bin/find_spark_home.py", "load-spark-env.cmd": "/usr/local/bin/load-spark-env.cmd", "load-spark-env.sh": "/usr/local/bin/load-spark-env.sh", "make_genome": "/usr/local/bin/make_genome", "mango-notebook": "/usr/local/bin/mango-notebook", "mango-submit": "/usr/local/bin/mango-submit", "pyadam": "/usr/local/bin/pyadam", "pyspark": "/usr/local/bin/pyspark", "pyspark.cmd": "/usr/local/bin/pyspark.cmd", "pyspark2.cmd": "/usr/local/bin/pyspark2.cmd", "run-example": "/usr/local/bin/run-example", "run-example.cmd": "/usr/local/bin/run-example.cmd", "spark-class": "/usr/local/bin/spark-class", "spark-class.cmd": "/usr/local/bin/spark-class.cmd", "spark-class2.cmd": "/usr/local/bin/spark-class2.cmd", "spark-shell": "/usr/local/bin/spark-shell", "spark-shell.cmd": "/usr/local/bin/spark-shell.cmd", "spark-shell2.cmd": "/usr/local/bin/spark-shell2.cmd", "spark-sql": "/usr/local/bin/spark-sql", "spark-sql.cmd": "/usr/local/bin/spark-sql.cmd", "spark-sql2.cmd": "/usr/local/bin/spark-sql2.cmd", "spark-submit": "/usr/local/bin/spark-submit", "spark-submit.cmd": "/usr/local/bin/spark-submit.cmd", "spark-submit2.cmd": "/usr/local/bin/spark-submit2.cmd", "sparkR": "/usr/local/bin/sparkR", "sparkR.cmd": "/usr/local/bin/sparkR.cmd", "sparkR2.cmd": "/usr/local/bin/sparkR2.cmd", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mango.
shpc-registry automated BioContainers addition for mango
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mango
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mango:0.0.5--pyh864c0ab_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mango/0.0.5--pyh864c0ab_4
$ module help quay.io/biocontainers/mango/0.0.5--pyh864c0ab_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mango-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mango-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mango-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mango-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mango-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mango-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adam-shell

```bash
$ singularity exec <container> /usr/local/bin/adam-shell
$ podman run --it --rm --entrypoint /usr/local/bin/adam-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adam-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adam-submit

```bash
$ singularity exec <container> /usr/local/bin/adam-submit
$ podman run --it --rm --entrypoint /usr/local/bin/adam-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adam-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adamR

```bash
$ singularity exec <container> /usr/local/bin/adamR
$ podman run --it --rm --entrypoint /usr/local/bin/adamR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adamR   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### docker-image-tool.sh

```bash
$ singularity exec <container> /usr/local/bin/docker-image-tool.sh
$ podman run --it --rm --entrypoint /usr/local/bin/docker-image-tool.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-image-tool.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-adam-assembly.sh

```bash
$ singularity exec <container> /usr/local/bin/find-adam-assembly.sh
$ podman run --it --rm --entrypoint /usr/local/bin/find-adam-assembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-adam-assembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-adam-egg.sh

```bash
$ singularity exec <container> /usr/local/bin/find-adam-egg.sh
$ podman run --it --rm --entrypoint /usr/local/bin/find-adam-egg.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-adam-egg.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-adam-home

```bash
$ singularity exec <container> /usr/local/bin/find-adam-home
$ podman run --it --rm --entrypoint /usr/local/bin/find-adam-home   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-adam-home   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-mango-assembly.sh

```bash
$ singularity exec <container> /usr/local/bin/find-mango-assembly.sh
$ podman run --it --rm --entrypoint /usr/local/bin/find-mango-assembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-mango-assembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-mango-home

```bash
$ singularity exec <container> /usr/local/bin/find-mango-home
$ podman run --it --rm --entrypoint /usr/local/bin/find-mango-home   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-mango-home   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### find-spark.sh

```bash
$ singularity exec <container> /usr/local/bin/find-spark.sh
$ podman run --it --rm --entrypoint /usr/local/bin/find-spark.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-spark.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_adam_home.py

```bash
$ singularity exec <container> /usr/local/bin/find_adam_home.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_adam_home.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_adam_home.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_spark_home.py

```bash
$ singularity exec <container> /usr/local/bin/find_spark_home.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_spark_home.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_spark_home.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### make_genome

```bash
$ singularity exec <container> /usr/local/bin/make_genome
$ podman run --it --rm --entrypoint /usr/local/bin/make_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mango-notebook

```bash
$ singularity exec <container> /usr/local/bin/mango-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/mango-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mango-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mango-submit

```bash
$ singularity exec <container> /usr/local/bin/mango-submit
$ podman run --it --rm --entrypoint /usr/local/bin/mango-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mango-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyadam

```bash
$ singularity exec <container> /usr/local/bin/pyadam
$ podman run --it --rm --entrypoint /usr/local/bin/pyadam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyadam   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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