---
layout: container
name:  "quay.io/biocontainers/deepvariant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepvariant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deepvariant/container.yaml"
updated_at: "2024-12-05 03:15:51.716343"
latest: "1.5.0--py36hf3e76ba_0"
container_url: "https://biocontainers.pro/tools/deepvariant"
aliases:
 - "bq"
 - "docker-credential-gcloud"
 - "dv_call_variants.py"
 - "dv_make_examples.py"
 - "dv_postprocess_variants.py"
 - "gcloud"
 - "gsutil"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "freeze_graph"
 - "google-oauthlib-tool"
 - "unzip"
 - "clhsdb"
 - "hsdb"
versions:
 - "1.4.0--py36hf3e76ba_0"
 - "1.5.0--py36hf3e76ba_0"
description: "shpc-registry automated BioContainers addition for deepvariant"
config: {"url": "https://biocontainers.pro/tools/deepvariant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepvariant", "latest": {"1.5.0--py36hf3e76ba_0": "sha256:1c34e133cd05dfe3c19468670c0011f6df639d7459710cced7cda2954f5a9da6"}, "tags": {"1.4.0--py36hf3e76ba_0": "sha256:3479d8ee8b670117922797e12b09ac06f34ed5a5ee9e766fa6aa0fb9d15ca5d3", "1.5.0--py36hf3e76ba_0": "sha256:1c34e133cd05dfe3c19468670c0011f6df639d7459710cced7cda2954f5a9da6"}, "docker": "quay.io/biocontainers/deepvariant", "aliases": {"bq": "/usr/local/bin/bq", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "dv_call_variants.py": "/usr/local/bin/dv_call_variants.py", "dv_make_examples.py": "/usr/local/bin/dv_make_examples.py", "dv_postprocess_variants.py": "/usr/local/bin/dv_postprocess_variants.py", "gcloud": "/usr/local/bin/gcloud", "gsutil": "/usr/local/bin/gsutil", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "freeze_graph": "/usr/local/bin/freeze_graph", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "unzip": "/usr/local/bin/unzip", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepvariant.
shpc-registry automated BioContainers addition for deepvariant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepvariant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepvariant:1.5.0--py36hf3e76ba_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepvariant/1.5.0--py36hf3e76ba_0
$ module help quay.io/biocontainers/deepvariant/1.5.0--py36hf3e76ba_0
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


#### gcloud

```bash
$ singularity exec <container> /usr/local/bin/gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsutil

```bash
$ singularity exec <container> /usr/local/bin/gsutil
$ podman run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freeze_graph

```bash
$ singularity exec <container> /usr/local/bin/freeze_graph
$ podman run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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