---
layout: container
name:  "quay.io/biocontainers/metavelvet-sl-pipeline"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metavelvet-sl-pipeline/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metavelvet-sl-pipeline/container.yaml"
updated_at: "2024-05-28 03:14:00.798465"
latest: "1.0--pl5.22.0_0"
container_url: "https://biocontainers.pro/tools/metavelvet-sl-pipeline"
aliases:
 - "FeatureExtract.pl"
 - "FeatureExtractPredict.pl"
 - "GenerateCommand.pl"
 - "ReadTaxon.pl"
 - "checkdata.py"
 - "dwgsim"
 - "dwgsim_eval"
 - "dwgsim_eval_plot.py"
 - "dwgsim_mut_to_vcf.pl"
 - "dwgsim_pileup_eval.pl"
 - "easy.py"
 - "eval.pl"
 - "grid.py"
 - "meta-velvete"
 - "meta-velvetg"
 - "metaphlan2.py"
 - "metaphlan2krona.py"
 - "run-annoIS.pl"
 - "subset.py"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "velvetg"
 - "velveth"
 - "config_data"
 - "easy_install-2.7"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
versions:
 - "1.0--pl5.22.0_0"
description: "shpc-registry automated BioContainers addition for metavelvet-sl-pipeline"
config: {"url": "https://biocontainers.pro/tools/metavelvet-sl-pipeline", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metavelvet-sl-pipeline", "latest": {"1.0--pl5.22.0_0": "sha256:ff4bbe216a58af3ab40afd13f3dd62c95bb0ad704443be1201d0671ff5ab7be9"}, "tags": {"1.0--pl5.22.0_0": "sha256:ff4bbe216a58af3ab40afd13f3dd62c95bb0ad704443be1201d0671ff5ab7be9"}, "docker": "quay.io/biocontainers/metavelvet-sl-pipeline", "aliases": {"FeatureExtract.pl": "/usr/local/bin/FeatureExtract.pl", "FeatureExtractPredict.pl": "/usr/local/bin/FeatureExtractPredict.pl", "GenerateCommand.pl": "/usr/local/bin/GenerateCommand.pl", "ReadTaxon.pl": "/usr/local/bin/ReadTaxon.pl", "checkdata.py": "/usr/local/bin/checkdata.py", "dwgsim": "/usr/local/bin/dwgsim", "dwgsim_eval": "/usr/local/bin/dwgsim_eval", "dwgsim_eval_plot.py": "/usr/local/bin/dwgsim_eval_plot.py", "dwgsim_mut_to_vcf.pl": "/usr/local/bin/dwgsim_mut_to_vcf.pl", "dwgsim_pileup_eval.pl": "/usr/local/bin/dwgsim_pileup_eval.pl", "easy.py": "/usr/local/bin/easy.py", "eval.pl": "/usr/local/bin/eval.pl", "grid.py": "/usr/local/bin/grid.py", "meta-velvete": "/usr/local/bin/meta-velvete", "meta-velvetg": "/usr/local/bin/meta-velvetg", "metaphlan2.py": "/usr/local/bin/metaphlan2.py", "metaphlan2krona.py": "/usr/local/bin/metaphlan2krona.py", "run-annoIS.pl": "/usr/local/bin/run-annoIS.pl", "subset.py": "/usr/local/bin/subset.py", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "config_data": "/usr/local/bin/config_data", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metavelvet-sl-pipeline.
shpc-registry automated BioContainers addition for metavelvet-sl-pipeline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metavelvet-sl-pipeline
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metavelvet-sl-pipeline:1.0--pl5.22.0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metavelvet-sl-pipeline/1.0--pl5.22.0_0
$ module help quay.io/biocontainers/metavelvet-sl-pipeline/1.0--pl5.22.0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metavelvet-sl-pipeline-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metavelvet-sl-pipeline-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metavelvet-sl-pipeline-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metavelvet-sl-pipeline-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metavelvet-sl-pipeline-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metavelvet-sl-pipeline-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FeatureExtract.pl

```bash
$ singularity exec <container> /usr/local/bin/FeatureExtract.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FeatureExtract.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FeatureExtract.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FeatureExtractPredict.pl

```bash
$ singularity exec <container> /usr/local/bin/FeatureExtractPredict.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FeatureExtractPredict.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FeatureExtractPredict.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenerateCommand.pl

```bash
$ singularity exec <container> /usr/local/bin/GenerateCommand.pl
$ podman run --it --rm --entrypoint /usr/local/bin/GenerateCommand.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenerateCommand.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReadTaxon.pl

```bash
$ singularity exec <container> /usr/local/bin/ReadTaxon.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ReadTaxon.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReadTaxon.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkdata.py

```bash
$ singularity exec <container> /usr/local/bin/checkdata.py
$ podman run --it --rm --entrypoint /usr/local/bin/checkdata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkdata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim

```bash
$ singularity exec <container> /usr/local/bin/dwgsim
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim_eval

```bash
$ singularity exec <container> /usr/local/bin/dwgsim_eval
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim_eval_plot.py

```bash
$ singularity exec <container> /usr/local/bin/dwgsim_eval_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim_eval_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim_eval_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim_mut_to_vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/dwgsim_mut_to_vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim_mut_to_vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim_mut_to_vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim_pileup_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/dwgsim_pileup_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim_pileup_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim_pileup_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy.py

```bash
$ singularity exec <container> /usr/local/bin/easy.py
$ podman run --it --rm --entrypoint /usr/local/bin/easy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval.pl

```bash
$ singularity exec <container> /usr/local/bin/eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grid.py

```bash
$ singularity exec <container> /usr/local/bin/grid.py
$ podman run --it --rm --entrypoint /usr/local/bin/grid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meta-velvete

```bash
$ singularity exec <container> /usr/local/bin/meta-velvete
$ podman run --it --rm --entrypoint /usr/local/bin/meta-velvete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meta-velvete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meta-velvetg

```bash
$ singularity exec <container> /usr/local/bin/meta-velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/meta-velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meta-velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphlan2.py

```bash
$ singularity exec <container> /usr/local/bin/metaphlan2.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaphlan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphlan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphlan2krona.py

```bash
$ singularity exec <container> /usr/local/bin/metaphlan2krona.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaphlan2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphlan2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-annoIS.pl

```bash
$ singularity exec <container> /usr/local/bin/run-annoIS.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-annoIS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-annoIS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subset.py

```bash
$ singularity exec <container> /usr/local/bin/subset.py
$ podman run --it --rm --entrypoint /usr/local/bin/subset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
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