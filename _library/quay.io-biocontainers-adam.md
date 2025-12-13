---
layout: container
name:  "quay.io/biocontainers/adam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/adam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/adam/container.yaml"
updated_at: "2025-12-13 04:00:35.384754"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/adam"
aliases:
 - "adam-shell"
 - "adam-submit"
 - "beeline"
 - "beeline.cmd"
 - "csv-import"
 - "docker-image-tool.sh"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "find-spark-home"
 - "find-spark-home.cmd"
 - "find_spark_home.py"
 - "load-spark-env.cmd"
 - "load-spark-env.sh"
 - "orc-memory"
 - "orc-scan"
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
 - "timezone-dump"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "plasma-store-server"
 - "plasma_store"
 - "sha256_profile"
 - "gflags_completions.sh"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
versions:
 - "1.0--hdfd78af_0"
 - "1.0.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for adam"
config: {"url": "https://biocontainers.pro/tools/adam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for adam", "latest": {"1.0.1--hdfd78af_0": "sha256:08001768f3f72844d062ebd3b03058774d4ad989de12a5ddde4e207d94886a60"}, "tags": {"1.0--hdfd78af_0": "sha256:25971a9e9ebcf48a23f085e2beef3317c65edc6bd459bb707677039e7b895f54", "1.0.1--hdfd78af_0": "sha256:08001768f3f72844d062ebd3b03058774d4ad989de12a5ddde4e207d94886a60"}, "docker": "quay.io/biocontainers/adam", "aliases": {"adam-shell": "/usr/local/bin/adam-shell", "adam-submit": "/usr/local/bin/adam-submit", "beeline": "/usr/local/bin/beeline", "beeline.cmd": "/usr/local/bin/beeline.cmd", "csv-import": "/usr/local/bin/csv-import", "docker-image-tool.sh": "/usr/local/bin/docker-image-tool.sh", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "find-spark-home": "/usr/local/bin/find-spark-home", "find-spark-home.cmd": "/usr/local/bin/find-spark-home.cmd", "find_spark_home.py": "/usr/local/bin/find_spark_home.py", "load-spark-env.cmd": "/usr/local/bin/load-spark-env.cmd", "load-spark-env.sh": "/usr/local/bin/load-spark-env.sh", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "pyspark": "/usr/local/bin/pyspark", "pyspark.cmd": "/usr/local/bin/pyspark.cmd", "pyspark2.cmd": "/usr/local/bin/pyspark2.cmd", "run-example": "/usr/local/bin/run-example", "run-example.cmd": "/usr/local/bin/run-example.cmd", "spark-class": "/usr/local/bin/spark-class", "spark-class.cmd": "/usr/local/bin/spark-class.cmd", "spark-class2.cmd": "/usr/local/bin/spark-class2.cmd", "spark-shell": "/usr/local/bin/spark-shell", "spark-shell.cmd": "/usr/local/bin/spark-shell.cmd", "spark-shell2.cmd": "/usr/local/bin/spark-shell2.cmd", "spark-sql": "/usr/local/bin/spark-sql", "spark-sql.cmd": "/usr/local/bin/spark-sql.cmd", "spark-sql2.cmd": "/usr/local/bin/spark-sql2.cmd", "spark-submit": "/usr/local/bin/spark-submit", "spark-submit.cmd": "/usr/local/bin/spark-submit.cmd", "spark-submit2.cmd": "/usr/local/bin/spark-submit2.cmd", "sparkR": "/usr/local/bin/sparkR", "sparkR.cmd": "/usr/local/bin/sparkR.cmd", "sparkR2.cmd": "/usr/local/bin/sparkR2.cmd", "timezone-dump": "/usr/local/bin/timezone-dump", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "sha256_profile": "/usr/local/bin/sha256_profile", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/adam.
shpc-registry automated BioContainers addition for adam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/adam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/adam:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/adam/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/adam/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adam-inspect-deffile:

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


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-image-tool.sh

```bash
$ singularity exec <container> /usr/local/bin/docker-image-tool.sh
$ podman run --it --rm --entrypoint /usr/local/bin/docker-image-tool.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-image-tool.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-contents

```bash
$ singularity exec <container> /usr/local/bin/orc-contents
$ podman run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-metadata

```bash
$ singularity exec <container> /usr/local/bin/orc-metadata
$ podman run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-statistics

```bash
$ singularity exec <container> /usr/local/bin/orc-statistics
$ podman run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma-store-server

```bash
$ singularity exec <container> /usr/local/bin/plasma-store-server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sha256_profile

```bash
$ singularity exec <container> /usr/local/bin/sha256_profile
$ podman run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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