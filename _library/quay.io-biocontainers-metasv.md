---
layout: container
name:  "quay.io/biocontainers/metasv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metasv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metasv/container.yaml"
updated_at: "2023-10-13 02:45:33.890104"
latest: "0.5.4--py27h9801fc8_4"
container_url: "https://biocontainers.pro/tools/metasv"
aliases:
 - "age_align"
 - "annotate_vcf_bam.py"
 - "pybedtools_demo.py"
 - "run_metasv.py"
 - "run_metasv_age.py"
 - "run_metasv_bed2vcf.py"
 - "run_metasv_sc_analysis.py"
 - "svtool_to_vcf.py"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "mag-improve"
 - "spades-convert-bin-to-fasta"
 - "spades-gsimplifier"
 - "spades-kmer-estimating"
 - "spades-read-filter"
 - "spaligner"
 - "spades-bwa"
 - "spades-core"
versions:
 - "0.5.4--py27h9801fc8_4"
description: "shpc-registry automated BioContainers addition for metasv"
config: {"url": "https://biocontainers.pro/tools/metasv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metasv", "latest": {"0.5.4--py27h9801fc8_4": "sha256:3da7a16717e840af039661fcdca68ab4c03b425149462555169c788a43ce46c9"}, "tags": {"0.5.4--py27h9801fc8_4": "sha256:3da7a16717e840af039661fcdca68ab4c03b425149462555169c788a43ce46c9"}, "docker": "quay.io/biocontainers/metasv", "aliases": {"age_align": "/usr/local/bin/age_align", "annotate_vcf_bam.py": "/usr/local/bin/annotate_vcf_bam.py", "pybedtools_demo.py": "/usr/local/bin/pybedtools_demo.py", "run_metasv.py": "/usr/local/bin/run_metasv.py", "run_metasv_age.py": "/usr/local/bin/run_metasv_age.py", "run_metasv_bed2vcf.py": "/usr/local/bin/run_metasv_bed2vcf.py", "run_metasv_sc_analysis.py": "/usr/local/bin/run_metasv_sc_analysis.py", "svtool_to_vcf.py": "/usr/local/bin/svtool_to_vcf.py", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "mag-improve": "/usr/local/bin/mag-improve", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter", "spaligner": "/usr/local/bin/spaligner", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metasv.
shpc-registry automated BioContainers addition for metasv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metasv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metasv:0.5.4--py27h9801fc8_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metasv/0.5.4--py27h9801fc8_4
$ module help quay.io/biocontainers/metasv/0.5.4--py27h9801fc8_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metasv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metasv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metasv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metasv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metasv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metasv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### age_align

```bash
$ singularity exec <container> /usr/local/bin/age_align
$ podman run --it --rm --entrypoint /usr/local/bin/age_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/age_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate_vcf_bam.py

```bash
$ singularity exec <container> /usr/local/bin/annotate_vcf_bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_vcf_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_vcf_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools_demo.py

```bash
$ singularity exec <container> /usr/local/bin/pybedtools_demo.py
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools_demo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools_demo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_metasv.py

```bash
$ singularity exec <container> /usr/local/bin/run_metasv.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_metasv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_metasv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_metasv_age.py

```bash
$ singularity exec <container> /usr/local/bin/run_metasv_age.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_metasv_age.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_metasv_age.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_metasv_bed2vcf.py

```bash
$ singularity exec <container> /usr/local/bin/run_metasv_bed2vcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_metasv_bed2vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_metasv_bed2vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_metasv_sc_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/run_metasv_sc_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_metasv_sc_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_metasv_sc_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtool_to_vcf.py

```bash
$ singularity exec <container> /usr/local/bin/svtool_to_vcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/svtool_to_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtool_to_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag-improve

```bash
$ singularity exec <container> /usr/local/bin/mag-improve
$ podman run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier

```bash
$ singularity exec <container> /usr/local/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating

```bash
$ singularity exec <container> /usr/local/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /usr/local/bin/spades-read-filter
$ podman run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /usr/local/bin/spaligner
$ podman run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-bwa

```bash
$ singularity exec <container> /usr/local/bin/spades-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core

```bash
$ singularity exec <container> /usr/local/bin/spades-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
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