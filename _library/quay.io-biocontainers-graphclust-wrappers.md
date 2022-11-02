---
layout: container
name:  "quay.io/biocontainers/graphclust-wrappers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphclust-wrappers/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/graphclust-wrappers/container.yaml"
updated_at: "2022-11-02 00:28:07.906239"
latest: "0.6.0--2"
container_url: "https://biocontainers.pro/tools/graphclust-wrappers"
aliases:
 - "NSPDK_candidateClusters.pl"
 - "NSPDK_sparseVect.pl"
 - "aggregate_align_metrics.py"
 - "alifold.pl"
 - "clustal_to_alma.py"
 - "extract_conservation_metrics.py"
 - "fasta2shrep_gspan.pl"
 - "foldFasta.pl"
 - "gc_align_clusters.pl"
 - "gc_res.pl"
 - "gc_res_noalign.pl"
 - "glob_res.pl"
 - "locARNAGraphClust.pl"
 - "mloc2stockholm.pl"
 - "newpreMlocarna.pl"
 - "preprocessing.pl"
 - "rnaclustScores2Dist.pl"
 - "scoreAln.pl"
 - "structure_2_gspan.pl"
 - "f2py3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "perl5.26.2"
versions:
 - "0.6.0--2"
description: "shpc-registry automated BioContainers addition for graphclust-wrappers"
config: {"url": "https://biocontainers.pro/tools/graphclust-wrappers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphclust-wrappers", "latest": {"0.6.0--2": "sha256:0104aa7c734d5f49bd7368f459ec38e97176af369d70f888ea9e00b5c6dfa8e8"}, "tags": {"0.6.0--2": "sha256:0104aa7c734d5f49bd7368f459ec38e97176af369d70f888ea9e00b5c6dfa8e8"}, "docker": "quay.io/biocontainers/graphclust-wrappers", "aliases": {"NSPDK_candidateClusters.pl": "/usr/local/bin/NSPDK_candidateClusters.pl", "NSPDK_sparseVect.pl": "/usr/local/bin/NSPDK_sparseVect.pl", "aggregate_align_metrics.py": "/usr/local/bin/aggregate_align_metrics.py", "alifold.pl": "/usr/local/bin/alifold.pl", "clustal_to_alma.py": "/usr/local/bin/clustal_to_alma.py", "extract_conservation_metrics.py": "/usr/local/bin/extract_conservation_metrics.py", "fasta2shrep_gspan.pl": "/usr/local/bin/fasta2shrep_gspan.pl", "foldFasta.pl": "/usr/local/bin/foldFasta.pl", "gc_align_clusters.pl": "/usr/local/bin/gc_align_clusters.pl", "gc_res.pl": "/usr/local/bin/gc_res.pl", "gc_res_noalign.pl": "/usr/local/bin/gc_res_noalign.pl", "glob_res.pl": "/usr/local/bin/glob_res.pl", "locARNAGraphClust.pl": "/usr/local/bin/locARNAGraphClust.pl", "mloc2stockholm.pl": "/usr/local/bin/mloc2stockholm.pl", "newpreMlocarna.pl": "/usr/local/bin/newpreMlocarna.pl", "preprocessing.pl": "/usr/local/bin/preprocessing.pl", "rnaclustScores2Dist.pl": "/usr/local/bin/rnaclustScores2Dist.pl", "scoreAln.pl": "/usr/local/bin/scoreAln.pl", "structure_2_gspan.pl": "/usr/local/bin/structure_2_gspan.pl", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "perl5.26.2": "/usr/local/bin/perl5.26.2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphclust-wrappers.
shpc-registry automated BioContainers addition for graphclust-wrappers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphclust-wrappers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphclust-wrappers:0.6.0--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphclust-wrappers/0.6.0--2
$ module help quay.io/biocontainers/graphclust-wrappers/0.6.0--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphclust-wrappers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphclust-wrappers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphclust-wrappers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphclust-wrappers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphclust-wrappers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphclust-wrappers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NSPDK_candidateClusters.pl

```bash
$ singularity exec <container> /usr/local/bin/NSPDK_candidateClusters.pl
$ podman run --it --rm --entrypoint /usr/local/bin/NSPDK_candidateClusters.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NSPDK_candidateClusters.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NSPDK_sparseVect.pl

```bash
$ singularity exec <container> /usr/local/bin/NSPDK_sparseVect.pl
$ podman run --it --rm --entrypoint /usr/local/bin/NSPDK_sparseVect.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NSPDK_sparseVect.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_align_metrics.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_align_metrics.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_align_metrics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_align_metrics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alifold.pl

```bash
$ singularity exec <container> /usr/local/bin/alifold.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alifold.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alifold.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustal_to_alma.py

```bash
$ singularity exec <container> /usr/local/bin/clustal_to_alma.py
$ podman run --it --rm --entrypoint /usr/local/bin/clustal_to_alma.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustal_to_alma.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_conservation_metrics.py

```bash
$ singularity exec <container> /usr/local/bin/extract_conservation_metrics.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_conservation_metrics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_conservation_metrics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2shrep_gspan.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta2shrep_gspan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2shrep_gspan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2shrep_gspan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### foldFasta.pl

```bash
$ singularity exec <container> /usr/local/bin/foldFasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/foldFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc_align_clusters.pl

```bash
$ singularity exec <container> /usr/local/bin/gc_align_clusters.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gc_align_clusters.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc_align_clusters.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc_res.pl

```bash
$ singularity exec <container> /usr/local/bin/gc_res.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gc_res.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc_res.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc_res_noalign.pl

```bash
$ singularity exec <container> /usr/local/bin/gc_res_noalign.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gc_res_noalign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc_res_noalign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glob_res.pl

```bash
$ singularity exec <container> /usr/local/bin/glob_res.pl
$ podman run --it --rm --entrypoint /usr/local/bin/glob_res.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glob_res.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locARNAGraphClust.pl

```bash
$ singularity exec <container> /usr/local/bin/locARNAGraphClust.pl
$ podman run --it --rm --entrypoint /usr/local/bin/locARNAGraphClust.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locARNAGraphClust.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mloc2stockholm.pl

```bash
$ singularity exec <container> /usr/local/bin/mloc2stockholm.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mloc2stockholm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mloc2stockholm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newpreMlocarna.pl

```bash
$ singularity exec <container> /usr/local/bin/newpreMlocarna.pl
$ podman run --it --rm --entrypoint /usr/local/bin/newpreMlocarna.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newpreMlocarna.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocessing.pl

```bash
$ singularity exec <container> /usr/local/bin/preprocessing.pl
$ podman run --it --rm --entrypoint /usr/local/bin/preprocessing.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocessing.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaclustScores2Dist.pl

```bash
$ singularity exec <container> /usr/local/bin/rnaclustScores2Dist.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnaclustScores2Dist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaclustScores2Dist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scoreAln.pl

```bash
$ singularity exec <container> /usr/local/bin/scoreAln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/scoreAln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scoreAln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### structure_2_gspan.pl

```bash
$ singularity exec <container> /usr/local/bin/structure_2_gspan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/structure_2_gspan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structure_2_gspan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
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