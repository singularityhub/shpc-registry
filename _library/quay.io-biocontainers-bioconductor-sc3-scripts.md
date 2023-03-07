---
layout: container
name:  "quay.io/biocontainers/bioconductor-sc3-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sc3-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sc3-scripts/container.yaml"
updated_at: "2023-03-07 03:40:20.244556"
latest: "0.0.3--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sc3-scripts"
aliases:
 - "bioconductor-sc3-scripts-post-install-tests.bats"
 - "bioconductor-sc3-scripts-post-install-tests.sh"
 - "bioconductor-scater-scripts-post-install-tests.bats"
 - "bioconductor-scater-scripts-post-install-tests.sh"
 - "bioconductor-singlecellexperiment-scripts-post-install-tests.sh"
 - "sc3-sc3-calc-biology.R"
 - "sc3-sc3-calc-consens.R"
 - "sc3-sc3-calc-dists.R"
 - "sc3-sc3-calc-transfs.R"
 - "sc3-sc3-estimate-k.R"
 - "sc3-sc3-kmeans.R"
 - "sc3-sc3-prepare.R"
 - "scater-calculate-cpm.R"
 - "scater-calculate-qc-metrics.R"
 - "scater-extract-qc-metric.R"
 - "scater-filter.R"
 - "scater-is-outlier.R"
 - "scater-normalize.R"
 - "scater-plot-reduced-dim.R"
 - "scater-run-pca.R"
 - "scater-run-tsne.R"
 - "singlecellexperiment-create-single-cell-experiment.R"
 - "singlecellexperiment-get-random-cells.R"
 - "singlecellexperiment-get-random-genes.R"
 - "conda_build.sh"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "0.0.3--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sc3-scripts"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sc3-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sc3-scripts", "latest": {"0.0.3--r351_0": "sha256:23e6f1d60732834065ef63c598cf687a2db0e538d44f79c6331e0310119cb54a"}, "tags": {"0.0.3--r351_0": "sha256:23e6f1d60732834065ef63c598cf687a2db0e538d44f79c6331e0310119cb54a"}, "docker": "quay.io/biocontainers/bioconductor-sc3-scripts", "aliases": {"bioconductor-sc3-scripts-post-install-tests.bats": "/usr/local/bin/bioconductor-sc3-scripts-post-install-tests.bats", "bioconductor-sc3-scripts-post-install-tests.sh": "/usr/local/bin/bioconductor-sc3-scripts-post-install-tests.sh", "bioconductor-scater-scripts-post-install-tests.bats": "/usr/local/bin/bioconductor-scater-scripts-post-install-tests.bats", "bioconductor-scater-scripts-post-install-tests.sh": "/usr/local/bin/bioconductor-scater-scripts-post-install-tests.sh", "bioconductor-singlecellexperiment-scripts-post-install-tests.sh": "/usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh", "sc3-sc3-calc-biology.R": "/usr/local/bin/sc3-sc3-calc-biology.R", "sc3-sc3-calc-consens.R": "/usr/local/bin/sc3-sc3-calc-consens.R", "sc3-sc3-calc-dists.R": "/usr/local/bin/sc3-sc3-calc-dists.R", "sc3-sc3-calc-transfs.R": "/usr/local/bin/sc3-sc3-calc-transfs.R", "sc3-sc3-estimate-k.R": "/usr/local/bin/sc3-sc3-estimate-k.R", "sc3-sc3-kmeans.R": "/usr/local/bin/sc3-sc3-kmeans.R", "sc3-sc3-prepare.R": "/usr/local/bin/sc3-sc3-prepare.R", "scater-calculate-cpm.R": "/usr/local/bin/scater-calculate-cpm.R", "scater-calculate-qc-metrics.R": "/usr/local/bin/scater-calculate-qc-metrics.R", "scater-extract-qc-metric.R": "/usr/local/bin/scater-extract-qc-metric.R", "scater-filter.R": "/usr/local/bin/scater-filter.R", "scater-is-outlier.R": "/usr/local/bin/scater-is-outlier.R", "scater-normalize.R": "/usr/local/bin/scater-normalize.R", "scater-plot-reduced-dim.R": "/usr/local/bin/scater-plot-reduced-dim.R", "scater-run-pca.R": "/usr/local/bin/scater-run-pca.R", "scater-run-tsne.R": "/usr/local/bin/scater-run-tsne.R", "singlecellexperiment-create-single-cell-experiment.R": "/usr/local/bin/singlecellexperiment-create-single-cell-experiment.R", "singlecellexperiment-get-random-cells.R": "/usr/local/bin/singlecellexperiment-get-random-cells.R", "singlecellexperiment-get-random-genes.R": "/usr/local/bin/singlecellexperiment-get-random-genes.R", "conda_build.sh": "/usr/local/bin/conda_build.sh", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sc3-scripts.
shpc-registry automated BioContainers addition for bioconductor-sc3-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sc3-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sc3-scripts:0.0.3--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sc3-scripts/0.0.3--r351_0
$ module help quay.io/biocontainers/bioconductor-sc3-scripts/0.0.3--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sc3-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sc3-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sc3-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sc3-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sc3-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sc3-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioconductor-sc3-scripts-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/bioconductor-sc3-scripts-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/bioconductor-sc3-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconductor-sc3-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconductor-sc3-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/bioconductor-sc3-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bioconductor-sc3-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconductor-sc3-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconductor-scater-scripts-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/bioconductor-scater-scripts-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/bioconductor-scater-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconductor-scater-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconductor-scater-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/bioconductor-scater-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bioconductor-scater-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconductor-scater-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconductor-singlecellexperiment-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-calc-biology.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-calc-biology.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-biology.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-biology.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-calc-consens.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-calc-consens.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-consens.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-consens.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-calc-dists.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-calc-dists.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-dists.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-dists.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-calc-transfs.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-calc-transfs.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-transfs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-calc-transfs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-estimate-k.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-estimate-k.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-estimate-k.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-estimate-k.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-kmeans.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-kmeans.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-kmeans.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-kmeans.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc3-sc3-prepare.R

```bash
$ singularity exec <container> /usr/local/bin/sc3-sc3-prepare.R
$ podman run --it --rm --entrypoint /usr/local/bin/sc3-sc3-prepare.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc3-sc3-prepare.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-calculate-cpm.R

```bash
$ singularity exec <container> /usr/local/bin/scater-calculate-cpm.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-calculate-cpm.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-calculate-cpm.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-calculate-qc-metrics.R

```bash
$ singularity exec <container> /usr/local/bin/scater-calculate-qc-metrics.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-calculate-qc-metrics.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-calculate-qc-metrics.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-extract-qc-metric.R

```bash
$ singularity exec <container> /usr/local/bin/scater-extract-qc-metric.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-extract-qc-metric.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-extract-qc-metric.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-filter.R

```bash
$ singularity exec <container> /usr/local/bin/scater-filter.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-filter.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-filter.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-is-outlier.R

```bash
$ singularity exec <container> /usr/local/bin/scater-is-outlier.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-is-outlier.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-is-outlier.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-normalize.R

```bash
$ singularity exec <container> /usr/local/bin/scater-normalize.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-normalize.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-normalize.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-plot-reduced-dim.R

```bash
$ singularity exec <container> /usr/local/bin/scater-plot-reduced-dim.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-plot-reduced-dim.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-plot-reduced-dim.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-run-pca.R

```bash
$ singularity exec <container> /usr/local/bin/scater-run-pca.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-run-pca.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-run-pca.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scater-run-tsne.R

```bash
$ singularity exec <container> /usr/local/bin/scater-run-tsne.R
$ podman run --it --rm --entrypoint /usr/local/bin/scater-run-tsne.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scater-run-tsne.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlecellexperiment-create-single-cell-experiment.R

```bash
$ singularity exec <container> /usr/local/bin/singlecellexperiment-create-single-cell-experiment.R
$ podman run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-create-single-cell-experiment.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-create-single-cell-experiment.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlecellexperiment-get-random-cells.R

```bash
$ singularity exec <container> /usr/local/bin/singlecellexperiment-get-random-cells.R
$ podman run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlecellexperiment-get-random-genes.R

```bash
$ singularity exec <container> /usr/local/bin/singlecellexperiment-get-random-genes.R
$ podman run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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