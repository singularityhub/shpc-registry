---
layout: container
name:  "quay.io/biocontainers/scran-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scran-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scran-cli/container.yaml"
updated_at: "2023-05-15 04:06:57.139941"
latest: "v0.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/scran-cli"
aliases:
 - "dropletutils-barcoderanks.R"
 - "dropletutils-downsample-matrix.R"
 - "dropletutils-empty-drops.R"
 - "dropletutils-make-test-sdrf.R"
 - "dropletutils-read-10x-counts.R"
 - "dropletutils-scripts-post-install-tests.bats"
 - "dropletutils-scripts-post-install-tests.sh"
 - "igraph_extract_clusters.R"
 - "old-scran-cli-filter-sce.R"
 - "scran-build-snn-graph.R"
 - "scran-cli-filter-sce.R"
 - "scran-compute-spike-factors.R"
 - "scran-compute-sum-factors.R"
 - "scran-convert-to.R"
 - "scran-correlate-genes.R"
 - "scran-correlate-pairs.R"
 - "scran-denoise-pca.R"
 - "scran-find-markers.R"
 - "scran-get-clustered-pcs.R"
 - "scran-model-gene-var-with-spikes.R"
 - "scran-model-gene-var.R"
 - "scran-trend-var.R"
 - "scran_post_install_tests.bats"
 - "scran_post_install_tests.sh"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "v0.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for scran-cli"
config: {"url": "https://biocontainers.pro/tools/scran-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scran-cli", "latest": {"v0.0.1--hdfd78af_1": "sha256:74ce0ecaea33088ac546dc617d29cf46bb890f08f7aed6a9de7b5c3f359af5bc"}, "tags": {"v0.0.1--hdfd78af_1": "sha256:74ce0ecaea33088ac546dc617d29cf46bb890f08f7aed6a9de7b5c3f359af5bc"}, "docker": "quay.io/biocontainers/scran-cli", "aliases": {"dropletutils-barcoderanks.R": "/usr/local/bin/dropletutils-barcoderanks.R", "dropletutils-downsample-matrix.R": "/usr/local/bin/dropletutils-downsample-matrix.R", "dropletutils-empty-drops.R": "/usr/local/bin/dropletutils-empty-drops.R", "dropletutils-make-test-sdrf.R": "/usr/local/bin/dropletutils-make-test-sdrf.R", "dropletutils-read-10x-counts.R": "/usr/local/bin/dropletutils-read-10x-counts.R", "dropletutils-scripts-post-install-tests.bats": "/usr/local/bin/dropletutils-scripts-post-install-tests.bats", "dropletutils-scripts-post-install-tests.sh": "/usr/local/bin/dropletutils-scripts-post-install-tests.sh", "igraph_extract_clusters.R": "/usr/local/bin/igraph_extract_clusters.R", "old-scran-cli-filter-sce.R": "/usr/local/bin/old-scran-cli-filter-sce.R", "scran-build-snn-graph.R": "/usr/local/bin/scran-build-snn-graph.R", "scran-cli-filter-sce.R": "/usr/local/bin/scran-cli-filter-sce.R", "scran-compute-spike-factors.R": "/usr/local/bin/scran-compute-spike-factors.R", "scran-compute-sum-factors.R": "/usr/local/bin/scran-compute-sum-factors.R", "scran-convert-to.R": "/usr/local/bin/scran-convert-to.R", "scran-correlate-genes.R": "/usr/local/bin/scran-correlate-genes.R", "scran-correlate-pairs.R": "/usr/local/bin/scran-correlate-pairs.R", "scran-denoise-pca.R": "/usr/local/bin/scran-denoise-pca.R", "scran-find-markers.R": "/usr/local/bin/scran-find-markers.R", "scran-get-clustered-pcs.R": "/usr/local/bin/scran-get-clustered-pcs.R", "scran-model-gene-var-with-spikes.R": "/usr/local/bin/scran-model-gene-var-with-spikes.R", "scran-model-gene-var.R": "/usr/local/bin/scran-model-gene-var.R", "scran-trend-var.R": "/usr/local/bin/scran-trend-var.R", "scran_post_install_tests.bats": "/usr/local/bin/scran_post_install_tests.bats", "scran_post_install_tests.sh": "/usr/local/bin/scran_post_install_tests.sh", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scran-cli.
shpc-registry automated BioContainers addition for scran-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scran-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scran-cli:v0.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scran-cli/v0.0.1--hdfd78af_1
$ module help quay.io/biocontainers/scran-cli/v0.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scran-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scran-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scran-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scran-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scran-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scran-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dropletutils-barcoderanks.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-barcoderanks.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-barcoderanks.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-barcoderanks.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-downsample-matrix.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-downsample-matrix.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-downsample-matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-downsample-matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-empty-drops.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-empty-drops.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-empty-drops.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-empty-drops.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-make-test-sdrf.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-make-test-sdrf.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-make-test-sdrf.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-make-test-sdrf.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-read-10x-counts.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-read-10x-counts.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-read-10x-counts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-read-10x-counts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-scripts-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-scripts-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph_extract_clusters.R

```bash
$ singularity exec <container> /usr/local/bin/igraph_extract_clusters.R
$ podman run --it --rm --entrypoint /usr/local/bin/igraph_extract_clusters.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph_extract_clusters.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old-scran-cli-filter-sce.R

```bash
$ singularity exec <container> /usr/local/bin/old-scran-cli-filter-sce.R
$ podman run --it --rm --entrypoint /usr/local/bin/old-scran-cli-filter-sce.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old-scran-cli-filter-sce.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-build-snn-graph.R

```bash
$ singularity exec <container> /usr/local/bin/scran-build-snn-graph.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-build-snn-graph.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-build-snn-graph.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-cli-filter-sce.R

```bash
$ singularity exec <container> /usr/local/bin/scran-cli-filter-sce.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-cli-filter-sce.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-cli-filter-sce.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-compute-spike-factors.R

```bash
$ singularity exec <container> /usr/local/bin/scran-compute-spike-factors.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-compute-spike-factors.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-compute-spike-factors.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-compute-sum-factors.R

```bash
$ singularity exec <container> /usr/local/bin/scran-compute-sum-factors.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-compute-sum-factors.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-compute-sum-factors.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-convert-to.R

```bash
$ singularity exec <container> /usr/local/bin/scran-convert-to.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-convert-to.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-convert-to.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-correlate-genes.R

```bash
$ singularity exec <container> /usr/local/bin/scran-correlate-genes.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-correlate-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-correlate-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-correlate-pairs.R

```bash
$ singularity exec <container> /usr/local/bin/scran-correlate-pairs.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-correlate-pairs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-correlate-pairs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-denoise-pca.R

```bash
$ singularity exec <container> /usr/local/bin/scran-denoise-pca.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-denoise-pca.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-denoise-pca.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-find-markers.R

```bash
$ singularity exec <container> /usr/local/bin/scran-find-markers.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-find-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-find-markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-get-clustered-pcs.R

```bash
$ singularity exec <container> /usr/local/bin/scran-get-clustered-pcs.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-get-clustered-pcs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-get-clustered-pcs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-model-gene-var-with-spikes.R

```bash
$ singularity exec <container> /usr/local/bin/scran-model-gene-var-with-spikes.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-model-gene-var-with-spikes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-model-gene-var-with-spikes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-model-gene-var.R

```bash
$ singularity exec <container> /usr/local/bin/scran-model-gene-var.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-model-gene-var.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-model-gene-var.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran-trend-var.R

```bash
$ singularity exec <container> /usr/local/bin/scran-trend-var.R
$ podman run --it --rm --entrypoint /usr/local/bin/scran-trend-var.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran-trend-var.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran_post_install_tests.bats

```bash
$ singularity exec <container> /usr/local/bin/scran_post_install_tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/scran_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scran_post_install_tests.sh

```bash
$ singularity exec <container> /usr/local/bin/scran_post_install_tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scran_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scran_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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