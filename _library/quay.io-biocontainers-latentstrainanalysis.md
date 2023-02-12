---
layout: container
name:  "quay.io/biocontainers/latentstrainanalysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/latentstrainanalysis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/latentstrainanalysis/container.yaml"
updated_at: "2023-02-12 02:48:44.372392"
latest: "0.0.1--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/latentstrainanalysis"
aliases:
 - "HashCounting.sh"
 - "KmerSVDClustering.sh"
 - "ReadPartitioning.sh"
 - "pyro4-check-config"
 - "pyro4-flameserver"
 - "pyro4-httpgateway"
 - "pyro4-ns"
 - "pyro4-nsc"
 - "pyro4-test-echoserver"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
 - "glacier"
versions:
 - "0.0.1--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for latentstrainanalysis"
config: {"url": "https://biocontainers.pro/tools/latentstrainanalysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for latentstrainanalysis", "latest": {"0.0.1--hdfd78af_3": "sha256:c7ff1f84c134f0adc2751980cf13c83f2f58386155f0c612a4b1afc8ec3137ea"}, "tags": {"0.0.1--hdfd78af_3": "sha256:c7ff1f84c134f0adc2751980cf13c83f2f58386155f0c612a4b1afc8ec3137ea"}, "docker": "quay.io/biocontainers/latentstrainanalysis", "aliases": {"HashCounting.sh": "/usr/local/bin/HashCounting.sh", "KmerSVDClustering.sh": "/usr/local/bin/KmerSVDClustering.sh", "ReadPartitioning.sh": "/usr/local/bin/ReadPartitioning.sh", "pyro4-check-config": "/usr/local/bin/pyro4-check-config", "pyro4-flameserver": "/usr/local/bin/pyro4-flameserver", "pyro4-httpgateway": "/usr/local/bin/pyro4-httpgateway", "pyro4-ns": "/usr/local/bin/pyro4-ns", "pyro4-nsc": "/usr/local/bin/pyro4-nsc", "pyro4-test-echoserver": "/usr/local/bin/pyro4-test-echoserver", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file", "glacier": "/usr/local/bin/glacier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/latentstrainanalysis.
shpc-registry automated BioContainers addition for latentstrainanalysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/latentstrainanalysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/latentstrainanalysis:0.0.1--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/latentstrainanalysis/0.0.1--hdfd78af_3
$ module help quay.io/biocontainers/latentstrainanalysis/0.0.1--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### latentstrainanalysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### latentstrainanalysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### latentstrainanalysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### latentstrainanalysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### latentstrainanalysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### latentstrainanalysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HashCounting.sh

```bash
$ singularity exec <container> /usr/local/bin/HashCounting.sh
$ podman run --it --rm --entrypoint /usr/local/bin/HashCounting.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HashCounting.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerSVDClustering.sh

```bash
$ singularity exec <container> /usr/local/bin/KmerSVDClustering.sh
$ podman run --it --rm --entrypoint /usr/local/bin/KmerSVDClustering.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerSVDClustering.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReadPartitioning.sh

```bash
$ singularity exec <container> /usr/local/bin/ReadPartitioning.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ReadPartitioning.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReadPartitioning.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-check-config

```bash
$ singularity exec <container> /usr/local/bin/pyro4-check-config
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-check-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-check-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-flameserver

```bash
$ singularity exec <container> /usr/local/bin/pyro4-flameserver
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-flameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-flameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-httpgateway

```bash
$ singularity exec <container> /usr/local/bin/pyro4-httpgateway
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-httpgateway   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-httpgateway   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-ns

```bash
$ singularity exec <container> /usr/local/bin/pyro4-ns
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-ns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-ns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-nsc

```bash
$ singularity exec <container> /usr/local/bin/pyro4-nsc
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-nsc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-nsc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro4-test-echoserver

```bash
$ singularity exec <container> /usr/local/bin/pyro4-test-echoserver
$ podman run --it --rm --entrypoint /usr/local/bin/pyro4-test-echoserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro4-test-echoserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glacier

```bash
$ singularity exec <container> /usr/local/bin/glacier
$ podman run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
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