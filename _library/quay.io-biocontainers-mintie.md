---
layout: container
name:  "quay.io/biocontainers/mintie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mintie/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mintie/container.yaml"
updated_at: "2022-10-27 00:21:02.057892"
latest: "0.4.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mintie"
aliases:
 - "SOAPdenovo-Trans-127mer"
 - "SOAPdenovo-Trans-31mer"
 - "Xcalcmem.sh"
 - "bg-bpipe"
 - "bpipe"
 - "bpipe-groovy"
 - "bpipe-pbspro.sh"
 - "bpipe-slurm.sh"
 - "bpipe-torque.sh"
 - "bpipe-utils.sh"
 - "bulk-counts"
 - "fastuniq"
 - "gmap.nosimd"
 - "gmap_cat"
 - "gmapl.nosimd"
 - "groovy_script"
 - "gsnap.nosimd"
 - "gsnapl.nosimd"
 - "indexdb_cat"
 - "mintie"
 - "sc-counts"
 - "velocity-counts"
versions:
 - "0.4.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mintie"
config: {"url": "https://biocontainers.pro/tools/mintie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mintie", "latest": {"0.4.1--hdfd78af_0": "sha256:8cb2f1475e634fe4e14be3dacf39e37e0c33dc479b471a91399dc906093e6efb"}, "tags": {"0.4.1--hdfd78af_0": "sha256:8cb2f1475e634fe4e14be3dacf39e37e0c33dc479b471a91399dc906093e6efb"}, "docker": "quay.io/biocontainers/mintie", "aliases": {"SOAPdenovo-Trans-127mer": "/usr/local/bin/SOAPdenovo-Trans-127mer", "SOAPdenovo-Trans-31mer": "/usr/local/bin/SOAPdenovo-Trans-31mer", "Xcalcmem.sh": "/usr/local/bin/Xcalcmem.sh", "bg-bpipe": "/usr/local/bin/bg-bpipe", "bpipe": "/usr/local/bin/bpipe", "bpipe-groovy": "/usr/local/bin/bpipe-groovy", "bpipe-pbspro.sh": "/usr/local/bin/bpipe-pbspro.sh", "bpipe-slurm.sh": "/usr/local/bin/bpipe-slurm.sh", "bpipe-torque.sh": "/usr/local/bin/bpipe-torque.sh", "bpipe-utils.sh": "/usr/local/bin/bpipe-utils.sh", "bulk-counts": "/usr/local/bin/bulk-counts", "fastuniq": "/usr/local/bin/fastuniq", "gmap.nosimd": "/usr/local/bin/gmap.nosimd", "gmap_cat": "/usr/local/bin/gmap_cat", "gmapl.nosimd": "/usr/local/bin/gmapl.nosimd", "groovy_script": "/usr/local/bin/groovy_script", "gsnap.nosimd": "/usr/local/bin/gsnap.nosimd", "gsnapl.nosimd": "/usr/local/bin/gsnapl.nosimd", "indexdb_cat": "/usr/local/bin/indexdb_cat", "mintie": "/usr/local/bin/mintie", "sc-counts": "/usr/local/bin/sc-counts", "velocity-counts": "/usr/local/bin/velocity-counts"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mintie.
shpc-registry automated BioContainers addition for mintie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mintie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mintie:0.4.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mintie/0.4.1--hdfd78af_0
$ module help quay.io/biocontainers/mintie/0.4.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mintie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mintie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mintie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mintie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mintie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mintie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SOAPdenovo-Trans-127mer

```bash
$ singularity exec <container> /usr/local/bin/SOAPdenovo-Trans-127mer
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-127mer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-127mer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPdenovo-Trans-31mer

```bash
$ singularity exec <container> /usr/local/bin/SOAPdenovo-Trans-31mer
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-31mer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-31mer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Xcalcmem.sh

```bash
$ singularity exec <container> /usr/local/bin/Xcalcmem.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bg-bpipe

```bash
$ singularity exec <container> /usr/local/bin/bg-bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe

```bash
$ singularity exec <container> /usr/local/bin/bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-groovy

```bash
$ singularity exec <container> /usr/local/bin/bpipe-groovy
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-groovy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-groovy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-pbspro.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-pbspro.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-slurm.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-slurm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-torque.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-torque.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-utils.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-utils.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bulk-counts

```bash
$ singularity exec <container> /usr/local/bin/bulk-counts
$ podman run --it --rm --entrypoint /usr/local/bin/bulk-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bulk-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastuniq

```bash
$ singularity exec <container> /usr/local/bin/fastuniq
$ podman run --it --rm --entrypoint /usr/local/bin/fastuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groovy_script

```bash
$ singularity exec <container> /usr/local/bin/groovy_script
$ podman run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mintie

```bash
$ singularity exec <container> /usr/local/bin/mintie
$ podman run --it --rm --entrypoint /usr/local/bin/mintie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mintie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc-counts

```bash
$ singularity exec <container> /usr/local/bin/sc-counts
$ podman run --it --rm --entrypoint /usr/local/bin/sc-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velocity-counts

```bash
$ singularity exec <container> /usr/local/bin/velocity-counts
$ podman run --it --rm --entrypoint /usr/local/bin/velocity-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velocity-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
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