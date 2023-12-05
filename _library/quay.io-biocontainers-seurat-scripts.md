---
layout: container
name:  "quay.io/biocontainers/seurat-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seurat-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seurat-scripts/container.yaml"
updated_at: "2023-12-05 03:06:29.660545"
latest: "4.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/seurat-scripts"
aliases:
 - "r-seurat-scripts-post-install-tests.bats"
 - "r-seurat-scripts-post-install-tests.sh"
 - "seurat-classify-against-reference.R"
 - "seurat-convert.R"
 - "seurat-dim-plot.R"
 - "seurat-export-cellbrowser.R"
 - "seurat-filter-cells.R"
 - "seurat-find-clusters.R"
 - "seurat-find-conserved-markers.R"
 - "seurat-find-markers.R"
 - "seurat-find-neighbours.R"
 - "seurat-find-variable-genes.R"
 - "seurat-get-random-genes.R"
 - "seurat-hover-locator.R"
 - "seurat-integration.R"
 - "seurat-map-query.R"
 - "seurat-normalise-data.R"
 - "seurat-plot.R"
 - "seurat-read-10x.R"
 - "seurat-read.R"
 - "seurat-run-pca.R"
 - "seurat-run-tsne.R"
 - "seurat-run-umap.R"
 - "seurat-scale-data.R"
 - "seurat-select-integration-features.R"
 - "seurat-split-object.R"
 - "mirror_server"
 - "mirror_server_stop"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "pandoc"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
versions:
 - "4.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for seurat-scripts"
config: {"url": "https://biocontainers.pro/tools/seurat-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seurat-scripts", "latest": {"4.0.0--hdfd78af_0": "sha256:455f2f0024096890c38d29b2f36b73400806c943a0f9c4e091cb7b07fae9afa0"}, "tags": {"4.0.0--hdfd78af_0": "sha256:455f2f0024096890c38d29b2f36b73400806c943a0f9c4e091cb7b07fae9afa0"}, "docker": "quay.io/biocontainers/seurat-scripts", "aliases": {"r-seurat-scripts-post-install-tests.bats": "/usr/local/bin/r-seurat-scripts-post-install-tests.bats", "r-seurat-scripts-post-install-tests.sh": "/usr/local/bin/r-seurat-scripts-post-install-tests.sh", "seurat-classify-against-reference.R": "/usr/local/bin/seurat-classify-against-reference.R", "seurat-convert.R": "/usr/local/bin/seurat-convert.R", "seurat-dim-plot.R": "/usr/local/bin/seurat-dim-plot.R", "seurat-export-cellbrowser.R": "/usr/local/bin/seurat-export-cellbrowser.R", "seurat-filter-cells.R": "/usr/local/bin/seurat-filter-cells.R", "seurat-find-clusters.R": "/usr/local/bin/seurat-find-clusters.R", "seurat-find-conserved-markers.R": "/usr/local/bin/seurat-find-conserved-markers.R", "seurat-find-markers.R": "/usr/local/bin/seurat-find-markers.R", "seurat-find-neighbours.R": "/usr/local/bin/seurat-find-neighbours.R", "seurat-find-variable-genes.R": "/usr/local/bin/seurat-find-variable-genes.R", "seurat-get-random-genes.R": "/usr/local/bin/seurat-get-random-genes.R", "seurat-hover-locator.R": "/usr/local/bin/seurat-hover-locator.R", "seurat-integration.R": "/usr/local/bin/seurat-integration.R", "seurat-map-query.R": "/usr/local/bin/seurat-map-query.R", "seurat-normalise-data.R": "/usr/local/bin/seurat-normalise-data.R", "seurat-plot.R": "/usr/local/bin/seurat-plot.R", "seurat-read-10x.R": "/usr/local/bin/seurat-read-10x.R", "seurat-read.R": "/usr/local/bin/seurat-read.R", "seurat-run-pca.R": "/usr/local/bin/seurat-run-pca.R", "seurat-run-tsne.R": "/usr/local/bin/seurat-run-tsne.R", "seurat-run-umap.R": "/usr/local/bin/seurat-run-umap.R", "seurat-scale-data.R": "/usr/local/bin/seurat-scale-data.R", "seurat-select-integration-features.R": "/usr/local/bin/seurat-select-integration-features.R", "seurat-split-object.R": "/usr/local/bin/seurat-split-object.R", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "pandoc": "/usr/local/bin/pandoc", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seurat-scripts.
shpc-registry automated BioContainers addition for seurat-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seurat-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seurat-scripts:4.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seurat-scripts/4.0.0--hdfd78af_0
$ module help quay.io/biocontainers/seurat-scripts/4.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seurat-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seurat-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seurat-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seurat-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seurat-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seurat-scripts-inspect-deffile:

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


#### seurat-classify-against-reference.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-classify-against-reference.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-classify-against-reference.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-classify-against-reference.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-convert.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-convert.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-convert.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-convert.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-dim-plot.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-dim-plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-dim-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-dim-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-export-cellbrowser.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-export-cellbrowser.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-export-cellbrowser.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-export-cellbrowser.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seurat-find-conserved-markers.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-find-conserved-markers.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-find-conserved-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-find-conserved-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-find-markers.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-find-markers.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-find-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-find-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-find-neighbours.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-find-neighbours.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-find-neighbours.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-find-neighbours.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seurat-hover-locator.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-hover-locator.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-hover-locator.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-hover-locator.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-integration.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-integration.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-integration.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-integration.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-map-query.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-map-query.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-map-query.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-map-query.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-normalise-data.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-normalise-data.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-normalise-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-normalise-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-plot.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-read-10x.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-read-10x.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-read-10x.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-read-10x.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-read.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-read.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-read.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-read.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seurat-run-umap.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-run-umap.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-run-umap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-run-umap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-scale-data.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-scale-data.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-scale-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-scale-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-select-integration-features.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-select-integration-features.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-select-integration-features.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-select-integration-features.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seurat-split-object.R

```bash
$ singularity exec <container> /usr/local/bin/seurat-split-object.R
$ podman run --it --rm --entrypoint /usr/local/bin/seurat-split-object.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seurat-split-object.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
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