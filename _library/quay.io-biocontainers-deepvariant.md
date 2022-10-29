---
layout: container
name:  "quay.io/biocontainers/deepvariant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepvariant/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepvariant/container.yaml"
updated_at: "2022-10-29 05:40:51.834402"
latest: "1.4.0--py36hf3e76ba_0"
container_url: "https://biocontainers.pro/tools/deepvariant"
aliases:
 - "dv_call_variants.py"
 - "dv_make_examples.py"
 - "dv_postprocess_variants.py"
 - "2to3-3.6"
 - "appletviewer"
 - "bgzip"
 - "bq"
 - "chardetect"
 - "clhsdb"
 - "docker-credential-gcloud"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
versions:
 - "1.4.0--py36hf3e76ba_0"
description: "shpc-registry automated BioContainers addition for deepvariant"
config: {"url": "https://biocontainers.pro/tools/deepvariant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepvariant", "latest": {"1.4.0--py36hf3e76ba_0": "sha256:3479d8ee8b670117922797e12b09ac06f34ed5a5ee9e766fa6aa0fb9d15ca5d3"}, "tags": {"1.4.0--py36hf3e76ba_0": "sha256:3479d8ee8b670117922797e12b09ac06f34ed5a5ee9e766fa6aa0fb9d15ca5d3"}, "docker": "quay.io/biocontainers/deepvariant", "aliases": {"dv_call_variants.py": "/usr/local/bin/dv_call_variants.py", "dv_make_examples.py": "/usr/local/bin/dv_make_examples.py", "dv_postprocess_variants.py": "/usr/local/bin/dv_postprocess_variants.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "appletviewer": "/usr/local/bin/appletviewer", "bgzip": "/usr/local/bin/bgzip", "bq": "/usr/local/bin/bq", "chardetect": "/usr/local/bin/chardetect", "clhsdb": "/usr/local/bin/clhsdb", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepvariant.
shpc-registry automated BioContainers addition for deepvariant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepvariant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepvariant:1.4.0--py36hf3e76ba_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepvariant/1.4.0--py36hf3e76ba_0
$ module help quay.io/biocontainers/deepvariant/1.4.0--py36hf3e76ba_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepvariant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepvariant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepvariant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepvariant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepvariant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepvariant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dv_call_variants.py

```bash
$ singularity exec <container> /usr/local/bin/dv_call_variants.py
$ podman run --it --rm --entrypoint /usr/local/bin/dv_call_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dv_call_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dv_make_examples.py

```bash
$ singularity exec <container> /usr/local/bin/dv_make_examples.py
$ podman run --it --rm --entrypoint /usr/local/bin/dv_make_examples.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dv_make_examples.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dv_postprocess_variants.py

```bash
$ singularity exec <container> /usr/local/bin/dv_postprocess_variants.py
$ podman run --it --rm --entrypoint /usr/local/bin/dv_postprocess_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dv_postprocess_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bq

```bash
$ singularity exec <container> /usr/local/bin/bq
$ podman run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-credential-gcloud

```bash
$ singularity exec <container> /usr/local/bin/docker-credential-gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
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