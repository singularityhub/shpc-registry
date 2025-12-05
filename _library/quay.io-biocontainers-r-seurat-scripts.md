---
layout: container
name:  "quay.io/biocontainers/r-seurat-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-seurat-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-seurat-scripts/container.yaml"
updated_at: "2025-12-05 04:01:32.348245"
latest: "0.0.4--r341_2"
container_url: "https://biocontainers.pro/tools/r-seurat-scripts"
aliases:
 - "r-seurat-scripts-post-install-tests.bats"
 - "r-seurat-scripts-post-install-tests.sh"
 - "seurat-create-seurat-object.R"
 - "seurat-dim-plot.R"
 - "seurat-filter-cells.R"
 - "seurat-find-clusters.R"
 - "seurat-find-markers.R"
 - "seurat-find-variable-genes.R"
 - "seurat-get-random-genes.R"
 - "seurat-normalise-data.R"
 - "seurat-read-10x.R"
 - "seurat-run-pca.R"
 - "seurat-run-tsne.R"
 - "seurat-scale-data.R"
 - "conda_build.sh"
 - "jaotc"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
 - "pack200"
versions:
 - "0.0.4--r341_2"
description: "shpc-registry automated BioContainers addition for r-seurat-scripts"
config: {"url": "https://biocontainers.pro/tools/r-seurat-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-seurat-scripts", "latest": {"0.0.4--r341_2": "sha256:4b27228c2e275c7f231678f3d5b234c97f84aa7db14a120d3e3b04b3d5b5bf4d"}, "tags": {"0.0.4--r341_2": "sha256:4b27228c2e275c7f231678f3d5b234c97f84aa7db14a120d3e3b04b3d5b5bf4d"}, "docker": "quay.io/biocontainers/r-seurat-scripts", "aliases": {"r-seurat-scripts-post-install-tests.bats": "/usr/local/bin/r-seurat-scripts-post-install-tests.bats", "r-seurat-scripts-post-install-tests.sh": "/usr/local/bin/r-seurat-scripts-post-install-tests.sh", "seurat-create-seurat-object.R": "/usr/local/bin/seurat-create-seurat-object.R", "seurat-dim-plot.R": "/usr/local/bin/seurat-dim-plot.R", "seurat-filter-cells.R": "/usr/local/bin/seurat-filter-cells.R", "seurat-find-clusters.R": "/usr/local/bin/seurat-find-clusters.R", "seurat-find-markers.R": "/usr/local/bin/seurat-find-markers.R", "seurat-find-variable-genes.R": "/usr/local/bin/seurat-find-variable-genes.R", "seurat-get-random-genes.R": "/usr/local/bin/seurat-get-random-genes.R", "seurat-normalise-data.R": "/usr/local/bin/seurat-normalise-data.R", "seurat-read-10x.R": "/usr/local/bin/seurat-read-10x.R", "seurat-run-pca.R": "/usr/local/bin/seurat-run-pca.R", "seurat-run-tsne.R": "/usr/local/bin/seurat-run-tsne.R", "seurat-scale-data.R": "/usr/local/bin/seurat-scale-data.R", "conda_build.sh": "/usr/local/bin/conda_build.sh", "jaotc": "/usr/local/bin/jaotc", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs", "pack200": "/usr/local/bin/pack200"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-seurat-scripts.
shpc-registry automated BioContainers addition for r-seurat-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-seurat-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-seurat-scripts:0.0.4--r341_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-seurat-scripts/0.0.4--r341_2
$ module help quay.io/biocontainers/r-seurat-scripts/0.0.4--r341_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-seurat-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-seurat-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-seurat-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-seurat-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-seurat-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-seurat-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### r-seurat-scripts-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/r-seurat-scripts-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/r-seurat-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/r-seurat-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### r-seurat-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/r-seurat-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/r-seurat-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/r-seurat-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-create-seurat-object.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-create-seurat-object.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-create-seurat-object.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-create-seurat-object.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-dim-plot.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-dim-plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-dim-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-dim-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-filter-cells.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-filter-cells.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-filter-cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-filter-cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-find-clusters.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-find-clusters.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-find-clusters.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-find-clusters.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-find-markers.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-find-markers.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-find-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-find-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-find-variable-genes.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-find-variable-genes.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-find-variable-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-find-variable-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-get-random-genes.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-get-random-genes.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-get-random-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-get-random-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-normalise-data.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-normalise-data.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-normalise-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-normalise-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-read-10x.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-read-10x.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-read-10x.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-read-10x.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-run-pca.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-run-pca.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-run-pca.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-run-pca.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-run-tsne.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-run-tsne.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-run-tsne.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-run-tsne.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-scale-data.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-scale-data.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-scale-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-scale-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pack200

```bash
$ singularity exec <container> /usr/local/bin/pack200
$ podman run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
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