---
layout: container
name:  "quay.io/biocontainers/tbpore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tbpore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tbpore/container.yaml"
updated_at: "2024-12-26 03:26:28.302994"
latest: "0.7.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tbpore"
aliases:
 - "mongod"
 - "mongos"
 - "mykrobe"
 - "psdm"
 - "rasusa"
 - "resmoke.py"
 - "tbpore"
 - "seqkit"
 - "cyvcf2"
 - "x86_64-conda_cos7-linux-gnu-ld"
 - "gff2gff.py"
 - "coloredlogs"
 - "vcf_sample_filter.py"
 - "humanfriendly"
 - "vcf_filter.py"
 - "vcf_melt"
 - "sdust"
versions:
 - "0.2.0--pyhdfd78af_0"
 - "0.3.2--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_1"
 - "0.4.1--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.7.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for tbpore"
config: {"url": "https://biocontainers.pro/tools/tbpore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tbpore", "latest": {"0.7.1--pyhdfd78af_0": "sha256:6977e07950242c48e96681235c2dd0fb0df298b8119987e3896594a649b3abd5"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:90f2175de4dff91941656a28cfdf9d96cc2a4355b71644765c7366b9bac184e3", "0.3.2--pyhdfd78af_0": "sha256:5934d7743c724470beee8ef126133f277176f7df00353bff36a36fb7e3ac049b", "0.4.0--pyhdfd78af_1": "sha256:de945c08ab35e6cbb41202a396f6541fdfbdec06d3cbe389f63dddfa1bc840b8", "0.4.1--pyhdfd78af_0": "sha256:65318ab98f1ac137fd2c06cd200559086007ff3b9a0073f34696eef75a455225", "0.6.0--pyhdfd78af_0": "sha256:0da34a40fd62981dd1a14a6b455db6fba6284403070a566d869ef5ff4f0b810d", "0.5.0--pyhdfd78af_0": "sha256:f9549a346293511f5d1cc40fc91b1c2bc7568c50519011263e6982718b53705a", "0.7.0--pyhdfd78af_0": "sha256:148ca58fddd962644ec7672bd604d4a85c8cea04ce3a8cfdccc253c1c8bf82e8", "0.7.1--pyhdfd78af_0": "sha256:6977e07950242c48e96681235c2dd0fb0df298b8119987e3896594a649b3abd5"}, "docker": "quay.io/biocontainers/tbpore", "aliases": {"mongod": "/usr/local/bin/mongod", "mongos": "/usr/local/bin/mongos", "mykrobe": "/usr/local/bin/mykrobe", "psdm": "/usr/local/bin/psdm", "rasusa": "/usr/local/bin/rasusa", "resmoke.py": "/usr/local/bin/resmoke.py", "tbpore": "/usr/local/bin/tbpore", "seqkit": "/usr/local/bin/seqkit", "cyvcf2": "/usr/local/bin/cyvcf2", "x86_64-conda_cos7-linux-gnu-ld": "/usr/local/bin/x86_64-conda_cos7-linux-gnu-ld", "gff2gff.py": "/usr/local/bin/gff2gff.py", "coloredlogs": "/usr/local/bin/coloredlogs", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "humanfriendly": "/usr/local/bin/humanfriendly", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "sdust": "/usr/local/bin/sdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tbpore.
shpc-registry automated BioContainers addition for tbpore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tbpore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tbpore:0.7.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tbpore/0.7.1--pyhdfd78af_0
$ module help quay.io/biocontainers/tbpore/0.7.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tbpore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tbpore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tbpore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tbpore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tbpore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tbpore-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### psdm

```bash
$ singularity exec <container> /usr/local/bin/psdm
$ podman run --it --rm --entrypoint /usr/local/bin/psdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rasusa

```bash
$ singularity exec <container> /usr/local/bin/rasusa
$ podman run --it --rm --entrypoint /usr/local/bin/rasusa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rasusa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resmoke.py

```bash
$ singularity exec <container> /usr/local/bin/resmoke.py
$ podman run --it --rm --entrypoint /usr/local/bin/resmoke.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resmoke.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbpore

```bash
$ singularity exec <container> /usr/local/bin/tbpore
$ podman run --it --rm --entrypoint /usr/local/bin/tbpore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbpore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos7-linux-gnu-ld

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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