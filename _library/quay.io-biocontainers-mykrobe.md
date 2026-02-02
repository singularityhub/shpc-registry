---
layout: container
name:  "quay.io/biocontainers/mykrobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mykrobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mykrobe/container.yaml"
updated_at: "2026-02-02 05:17:30.722653"
latest: "0.13.0--py311h22b1866_5"
container_url: "https://biocontainers.pro/tools/mykrobe"
aliases:
 - "install_compass"
 - "mongo"
 - "mongod"
 - "mongos"
 - "mykrobe"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "idn2"
 - "f2py3.8"
 - "chardetect"
 - "wget"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
versions:
 - "0.9.0--py38h8e3bb3f_3"
 - "0.10.0--py37h09c1ff4_1"
 - "0.13.0--py38h2214202_0"
 - "0.12.2--py39h0163359_1"
 - "0.11.0--py36hcac48a8_1"
 - "0.10.0--py39h2add14b_1"
 - "0.9.0--py36h61628e2_3"
 - "0.13.0--py38h59a8061_3"
 - "0.13.0--py312h20b014d_4"
 - "0.13.0--py311h22b1866_5"
description: "shpc-registry automated BioContainers addition for mykrobe"
config: {"url": "https://biocontainers.pro/tools/mykrobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mykrobe", "latest": {"0.13.0--py311h22b1866_5": "sha256:4661c03a3186fed661c3fda8f332ea9f151abf6296fc44d36642b9afac023a5d"}, "tags": {"0.9.0--py38h8e3bb3f_3": "sha256:cad54cf1570ba39df553217c2589f294560ccf692f0c6d5682844b92e95e7a02", "0.10.0--py37h09c1ff4_1": "sha256:9900f495e67fedde41d4cdf02985cc282bef407331ca03669ae9f259e7dc2044", "0.13.0--py38h2214202_0": "sha256:3909ff340be1e590b968c365a6cb89b536e58b2b5756c48d6a4437ad6b848df5", "0.12.2--py39h0163359_1": "sha256:95b3ba7d6150c3d9bc82534886a15bb5ea7ddfbb64b818674182ad13d9052971", "0.11.0--py36hcac48a8_1": "sha256:d3da929c488cf15b541c4efeaabbac1e6cfa74908e2b78e1cfe69192b5a893fe", "0.10.0--py39h2add14b_1": "sha256:3a4505427de01ee2a9cf9c071cfa240fccea4b32a8d62f3cdcc1d6ef88c17a56", "0.9.0--py36h61628e2_3": "sha256:85ccc6f3ae429905f4ee3cf413aabea8b3fa072d5df30bbdf1ad7921ae8a42c4", "0.13.0--py38h59a8061_3": "sha256:3c61405c2dbc21179eec636531299d0f0ee1e2133a340bc2ac88274a1651dcd2", "0.13.0--py312h20b014d_4": "sha256:a1a7cb47ddd55554b13c67faa917617c9216ed50c62ceb242ff5959822982941", "0.13.0--py311h22b1866_5": "sha256:4661c03a3186fed661c3fda8f332ea9f151abf6296fc44d36642b9afac023a5d"}, "docker": "quay.io/biocontainers/mykrobe", "aliases": {"install_compass": "/usr/local/bin/install_compass", "mongo": "/usr/local/bin/mongo", "mongod": "/usr/local/bin/mongod", "mongos": "/usr/local/bin/mongos", "mykrobe": "/usr/local/bin/mykrobe", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "idn2": "/usr/local/bin/idn2", "f2py3.8": "/usr/local/bin/f2py3.8", "chardetect": "/usr/local/bin/chardetect", "wget": "/usr/local/bin/wget", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mykrobe.
shpc-registry automated BioContainers addition for mykrobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mykrobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mykrobe:0.13.0--py311h22b1866_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mykrobe/0.13.0--py311h22b1866_5
$ module help quay.io/biocontainers/mykrobe/0.13.0--py311h22b1866_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mykrobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mykrobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mykrobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mykrobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mykrobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mykrobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### install_compass

```bash
$ singularity exec <container> /usr/local/bin/install_compass
$ podman run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongo

```bash
$ singularity exec <container> /usr/local/bin/mongo
$ podman run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongod

```bash
$ singularity exec <container> /usr/local/bin/mongod
$ podman run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongos

```bash
$ singularity exec <container> /usr/local/bin/mongos
$ podman run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mykrobe

```bash
$ singularity exec <container> /usr/local/bin/mykrobe
$ podman run --it --rm --entrypoint /usr/local/bin/mykrobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mykrobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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