---
layout: container
name:  "quay.io/biocontainers/transgenescan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transgenescan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transgenescan/container.yaml"
updated_at: "2025-05-19 03:50:13.278924"
latest: "1.3.0--h7b50bb2_3"
container_url: "https://biocontainers.pro/tools/transgenescan"
aliases:
 - "FGS_gff.py"
 - "TransGeneScan"
 - "post_process.pl"
 - "processFragOut.py"
 - "run_TransGeneScan.pl"
versions:
 - "1.2.1--hec16e2b_3"
 - "1.3.0--hec16e2b_0"
 - "1.3.0--h031d066_2"
 - "1.3.0--h7b50bb2_3"
description: "shpc-registry automated BioContainers addition for transgenescan"
config: {"url": "https://biocontainers.pro/tools/transgenescan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transgenescan", "latest": {"1.3.0--h7b50bb2_3": "sha256:9de8a132013023e05f710c5cbeab3b85fea5cb7703a00e0f9eca5e7639aafb61"}, "tags": {"1.2.1--hec16e2b_3": "sha256:16d075a5ad7b30b49e7a521e4793a647702355742b7c61c0cdbd61924311c52b", "1.3.0--hec16e2b_0": "sha256:994327b77b349a58608a66df19f1934cb7744f101ae5d92953691280dcf2102d", "1.3.0--h031d066_2": "sha256:170c21dac4fc3dd978aaed4dd464d2ec27dd25d8b638efcc41e507c0c9332084", "1.3.0--h7b50bb2_3": "sha256:9de8a132013023e05f710c5cbeab3b85fea5cb7703a00e0f9eca5e7639aafb61"}, "docker": "quay.io/biocontainers/transgenescan", "aliases": {"FGS_gff.py": "/usr/local/bin/FGS_gff.py", "TransGeneScan": "/usr/local/bin/TransGeneScan", "post_process.pl": "/usr/local/bin/post_process.pl", "processFragOut.py": "/usr/local/bin/processFragOut.py", "run_TransGeneScan.pl": "/usr/local/bin/run_TransGeneScan.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transgenescan.
shpc-registry automated BioContainers addition for transgenescan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transgenescan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transgenescan:1.3.0--h7b50bb2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transgenescan/1.3.0--h7b50bb2_3
$ module help quay.io/biocontainers/transgenescan/1.3.0--h7b50bb2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transgenescan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transgenescan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transgenescan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transgenescan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transgenescan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transgenescan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FGS_gff.py

```bash
$ singularity exec <container> /usr/local/bin/FGS_gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/FGS_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FGS_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TransGeneScan

```bash
$ singularity exec <container> /usr/local/bin/TransGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/TransGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TransGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### post_process.pl

```bash
$ singularity exec <container> /usr/local/bin/post_process.pl
$ podman run --it --rm --entrypoint /usr/local/bin/post_process.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/post_process.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### processFragOut.py

```bash
$ singularity exec <container> /usr/local/bin/processFragOut.py
$ podman run --it --rm --entrypoint /usr/local/bin/processFragOut.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/processFragOut.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_TransGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_TransGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_TransGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_TransGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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