---
layout: container
name:  "quay.io/biocontainers/r-seurat-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-seurat-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-seurat-scripts/container.yaml"
updated_at: "2022-10-27 00:42:51.053460"
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
versions:
 - "0.0.4--r341_2"
description: "shpc-registry automated BioContainers addition for r-seurat-scripts"
config: {"url": "https://biocontainers.pro/tools/r-seurat-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-seurat-scripts", "latest": {"0.0.4--r341_2": "sha256:d097e23da3cb5fc3c72ed7454d1172c1962f92278de63b0b3512b59e380f0d11"}, "tags": {"0.0.4--r341_2": "sha256:d097e23da3cb5fc3c72ed7454d1172c1962f92278de63b0b3512b59e380f0d11"}, "docker": "quay.io/biocontainers/r-seurat-scripts", "aliases": {"r-seurat-scripts-post-install-tests.bats": "/usr/local/bin/r-seurat-scripts-post-install-tests.bats", "r-seurat-scripts-post-install-tests.sh": "/usr/local/bin/r-seurat-scripts-post-install-tests.sh", "seurat-create-seurat-object.R": "/usr/local/bin/seurat-create-seurat-object.R", "seurat-dim-plot.R": "/usr/local/bin/seurat-dim-plot.R", "seurat-filter-cells.R": "/usr/local/bin/seurat-filter-cells.R", "seurat-find-clusters.R": "/usr/local/bin/seurat-find-clusters.R", "seurat-find-markers.R": "/usr/local/bin/seurat-find-markers.R", "seurat-find-variable-genes.R": "/usr/local/bin/seurat-find-variable-genes.R", "seurat-get-random-genes.R": "/usr/local/bin/seurat-get-random-genes.R", "seurat-normalise-data.R": "/usr/local/bin/seurat-normalise-data.R", "seurat-read-10x.R": "/usr/local/bin/seurat-read-10x.R", "seurat-run-pca.R": "/usr/local/bin/seurat-run-pca.R", "seurat-run-tsne.R": "/usr/local/bin/seurat-run-tsne.R", "seurat-scale-data.R": "/usr/local/bin/seurat-scale-data.R"}}
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