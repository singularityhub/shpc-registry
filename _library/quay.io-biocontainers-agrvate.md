---
layout: container
name:  "quay.io/biocontainers/agrvate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/agrvate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/agrvate/container.yaml"
updated_at: "2025-10-31 03:50:01.517161"
latest: "1.0.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/agrvate"
aliases:
 - "agrvate"
 - "file"
 - "snippy"
 - "snippy-clean_full_aln"
 - "snippy-core"
 - "snippy-multi"
 - "snippy-vcf_extract_subs"
 - "snippy-vcf_report"
 - "snippy-vcf_to_tab"
 - "vcfnormalizesvs"
 - "vcfnull2ref"
 - "vcfunphase"
 - "snp-sites"
 - "filter-table"
 - "spdi2prod"
 - "vt"
 - "seqkit"
 - "plotBfst.R"
 - "plotHapLrt.R"
 - "plotHaplotypes.R"
 - "plotPfst.R"
 - "plotSmoothed.R"
versions:
 - "1.0.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for agrvate"
config: {"url": "https://biocontainers.pro/tools/agrvate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for agrvate", "latest": {"1.0.2--hdfd78af_0": "sha256:69a7f3d16d6641206a9c1dd09c5f1c3e68ace8e50c4593703dbff52399a5aa03"}, "tags": {"1.0.2--hdfd78af_0": "sha256:69a7f3d16d6641206a9c1dd09c5f1c3e68ace8e50c4593703dbff52399a5aa03"}, "docker": "quay.io/biocontainers/agrvate", "aliases": {"agrvate": "/usr/local/bin/agrvate", "file": "/usr/local/bin/file", "snippy": "/usr/local/bin/snippy", "snippy-clean_full_aln": "/usr/local/bin/snippy-clean_full_aln", "snippy-core": "/usr/local/bin/snippy-core", "snippy-multi": "/usr/local/bin/snippy-multi", "snippy-vcf_extract_subs": "/usr/local/bin/snippy-vcf_extract_subs", "snippy-vcf_report": "/usr/local/bin/snippy-vcf_report", "snippy-vcf_to_tab": "/usr/local/bin/snippy-vcf_to_tab", "vcfnormalizesvs": "/usr/local/bin/vcfnormalizesvs", "vcfnull2ref": "/usr/local/bin/vcfnull2ref", "vcfunphase": "/usr/local/bin/vcfunphase", "snp-sites": "/usr/local/bin/snp-sites", "filter-table": "/usr/local/bin/filter-table", "spdi2prod": "/usr/local/bin/spdi2prod", "vt": "/usr/local/bin/vt", "seqkit": "/usr/local/bin/seqkit", "plotBfst.R": "/usr/local/bin/plotBfst.R", "plotHapLrt.R": "/usr/local/bin/plotHapLrt.R", "plotHaplotypes.R": "/usr/local/bin/plotHaplotypes.R", "plotPfst.R": "/usr/local/bin/plotPfst.R", "plotSmoothed.R": "/usr/local/bin/plotSmoothed.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/agrvate.
shpc-registry automated BioContainers addition for agrvate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/agrvate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/agrvate:1.0.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/agrvate/1.0.2--hdfd78af_0
$ module help quay.io/biocontainers/agrvate/1.0.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### agrvate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### agrvate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### agrvate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### agrvate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### agrvate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### agrvate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### agrvate

```bash
$ singularity exec <container> /usr/local/bin/agrvate
$ podman run --it --rm --entrypoint /usr/local/bin/agrvate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agrvate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### file

```bash
$ singularity exec <container> /usr/local/bin/file
$ podman run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy

```bash
$ singularity exec <container> /usr/local/bin/snippy
$ podman run --it --rm --entrypoint /usr/local/bin/snippy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-clean_full_aln

```bash
$ singularity exec <container> /usr/local/bin/snippy-clean_full_aln
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-clean_full_aln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-clean_full_aln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-core

```bash
$ singularity exec <container> /usr/local/bin/snippy-core
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-multi

```bash
$ singularity exec <container> /usr/local/bin/snippy-multi
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-vcf_extract_subs

```bash
$ singularity exec <container> /usr/local/bin/snippy-vcf_extract_subs
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-vcf_extract_subs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-vcf_extract_subs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-vcf_report

```bash
$ singularity exec <container> /usr/local/bin/snippy-vcf_report
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-vcf_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-vcf_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-vcf_to_tab

```bash
$ singularity exec <container> /usr/local/bin/snippy-vcf_to_tab
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-vcf_to_tab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-vcf_to_tab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnormalizesvs

```bash
$ singularity exec <container> /usr/local/bin/vcfnormalizesvs
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnormalizesvs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnormalizesvs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnull2ref

```bash
$ singularity exec <container> /usr/local/bin/vcfnull2ref
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnull2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnull2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfunphase

```bash
$ singularity exec <container> /usr/local/bin/vcfunphase
$ podman run --it --rm --entrypoint /usr/local/bin/vcfunphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfunphase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-sites

```bash
$ singularity exec <container> /usr/local/bin/snp-sites
$ podman run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotBfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotBfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHapLrt.R

```bash
$ singularity exec <container> /usr/local/bin/plotHapLrt.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotHapLrt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHapLrt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHaplotypes.R

```bash
$ singularity exec <container> /usr/local/bin/plotHaplotypes.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotHaplotypes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHaplotypes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotPfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotPfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotPfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotPfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotSmoothed.R

```bash
$ singularity exec <container> /usr/local/bin/plotSmoothed.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotSmoothed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotSmoothed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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