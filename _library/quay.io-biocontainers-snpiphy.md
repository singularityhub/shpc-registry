---
layout: container
name:  "quay.io/biocontainers/snpiphy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snpiphy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snpiphy/container.yaml"
updated_at: "2023-11-24 03:07:53.353769"
latest: "0.5--py_0"
container_url: "https://biocontainers.pro/tools/snpiphy"
aliases:
 - "gubbins"
 - "run_gubbins.py"
 - "snippy"
 - "snippy-clean_full_aln"
 - "snippy-core"
 - "snippy-multi"
 - "snippy-vcf_extract_subs"
 - "snippy-vcf_report"
 - "snippy-vcf_to_tab"
 - "snpiphy"
 - "snpiphy_generate_input_list"
 - "vcfnormalizesvs"
 - "vcfnull2ref"
 - "vcfunphase"
 - "snp-sites"
 - "vt"
 - "plotBfst.R"
 - "plotHapLrt.R"
 - "plotHaplotypes.R"
 - "plotPfst.R"
 - "plotSmoothed.R"
 - "plotWCfst.R"
 - "plotXPEHH.R"
 - "plot_roc.r"
versions:
 - "0.5--py_0"
description: "shpc-registry automated BioContainers addition for snpiphy"
config: {"url": "https://biocontainers.pro/tools/snpiphy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snpiphy", "latest": {"0.5--py_0": "sha256:94a8355d83981da29efc47b2eb8bfcf35bc421cbd430aa37ef0104e451e7792a"}, "tags": {"0.5--py_0": "sha256:94a8355d83981da29efc47b2eb8bfcf35bc421cbd430aa37ef0104e451e7792a"}, "docker": "quay.io/biocontainers/snpiphy", "aliases": {"gubbins": "/usr/local/bin/gubbins", "run_gubbins.py": "/usr/local/bin/run_gubbins.py", "snippy": "/usr/local/bin/snippy", "snippy-clean_full_aln": "/usr/local/bin/snippy-clean_full_aln", "snippy-core": "/usr/local/bin/snippy-core", "snippy-multi": "/usr/local/bin/snippy-multi", "snippy-vcf_extract_subs": "/usr/local/bin/snippy-vcf_extract_subs", "snippy-vcf_report": "/usr/local/bin/snippy-vcf_report", "snippy-vcf_to_tab": "/usr/local/bin/snippy-vcf_to_tab", "snpiphy": "/usr/local/bin/snpiphy", "snpiphy_generate_input_list": "/usr/local/bin/snpiphy_generate_input_list", "vcfnormalizesvs": "/usr/local/bin/vcfnormalizesvs", "vcfnull2ref": "/usr/local/bin/vcfnull2ref", "vcfunphase": "/usr/local/bin/vcfunphase", "snp-sites": "/usr/local/bin/snp-sites", "vt": "/usr/local/bin/vt", "plotBfst.R": "/usr/local/bin/plotBfst.R", "plotHapLrt.R": "/usr/local/bin/plotHapLrt.R", "plotHaplotypes.R": "/usr/local/bin/plotHaplotypes.R", "plotPfst.R": "/usr/local/bin/plotPfst.R", "plotSmoothed.R": "/usr/local/bin/plotSmoothed.R", "plotWCfst.R": "/usr/local/bin/plotWCfst.R", "plotXPEHH.R": "/usr/local/bin/plotXPEHH.R", "plot_roc.r": "/usr/local/bin/plot_roc.r"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snpiphy.
shpc-registry automated BioContainers addition for snpiphy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snpiphy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snpiphy:0.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snpiphy/0.5--py_0
$ module help quay.io/biocontainers/snpiphy/0.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snpiphy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snpiphy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snpiphy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snpiphy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snpiphy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snpiphy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gubbins

```bash
$ singularity exec <container> /usr/local/bin/gubbins
$ podman run --it --rm --entrypoint /usr/local/bin/gubbins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gubbins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_gubbins.py

```bash
$ singularity exec <container> /usr/local/bin/run_gubbins.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_gubbins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_gubbins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### snpiphy

```bash
$ singularity exec <container> /usr/local/bin/snpiphy
$ podman run --it --rm --entrypoint /usr/local/bin/snpiphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpiphy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpiphy_generate_input_list

```bash
$ singularity exec <container> /usr/local/bin/snpiphy_generate_input_list
$ podman run --it --rm --entrypoint /usr/local/bin/snpiphy_generate_input_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpiphy_generate_input_list   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### plotWCfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotWCfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotWCfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotWCfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotXPEHH.R

```bash
$ singularity exec <container> /usr/local/bin/plotXPEHH.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotXPEHH.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotXPEHH.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_roc.r

```bash
$ singularity exec <container> /usr/local/bin/plot_roc.r
$ podman run --it --rm --entrypoint /usr/local/bin/plot_roc.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_roc.r   -v ${PWD} -w ${PWD} <container> -c " $@"
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