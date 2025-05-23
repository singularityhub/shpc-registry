---
layout: container
name:  "quay.io/biocontainers/sipros"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sipros/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sipros/container.yaml"
updated_at: "2025-05-23 03:27:21.900123"
latest: "4.02--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/sipros"
aliases:
 - "EnsembleScripts_sipros_ensemble_filtering"
 - "EnsembleScripts_sipros_peptides_assembling"
 - "EnsembleScripts_sipros_prepare_protein_database"
 - "EnsembleScripts_sipros_psm_tabulating"
 - "Raxport"
 - "Raxport.exe"
 - "SiprosEnsembleOMP"
 - "SiprosV4OMP"
 - "V4Scripts_ClusterSip"
 - "V4Scripts_getLabelPCTinEachFT"
 - "V4Scripts_getSpectraCountInEachFT"
 - "V4Scripts_makeDBforLabelSearch"
 - "V4Scripts_refineProteinFDR"
 - "V4Scripts_sipros_peptides_assembling"
 - "V4Scripts_sipros_peptides_filtering"
 - "aprofutil"
 - "configGenerator"
 - "copyConfigTemplate"
 - "mono-hang-watchdog"
 - "csc"
 - "csi"
 - "illinkanalyzer"
 - "vbc"
 - "mono-package-runtime"
 - "sgen-grep-binprot"
 - "al"
 - "al2"
 - "caspol"
 - "cccheck"
 - "ccrewrite"
 - "cert-sync"
 - "cert2spc"
 - "certmgr"
 - "chktrust"
 - "crlupdate"
 - "csharp"
 - "dmcs"
 - "dtd2rng"
 - "dtd2xsd"
 - "gacutil"
 - "gacutil2"
 - "genxs"
 - "httpcfg"
 - "ikdasm"
versions:
 - "4.01--hdfd78af_0"
 - "4.02--hdfd78af_1"
description: "singularity registry hpc automated addition for sipros"
config: {"url": "https://biocontainers.pro/tools/sipros", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sipros", "latest": {"4.02--hdfd78af_1": "sha256:65e08cd356d0f6310e9ce027c768bd4b829424f2be23f4878f56d836e612b4fe"}, "tags": {"4.01--hdfd78af_0": "sha256:9fa6d9d642eba6a678b76774a2b47e10426201fc06b3a0dfabf893702f88b831", "4.02--hdfd78af_1": "sha256:65e08cd356d0f6310e9ce027c768bd4b829424f2be23f4878f56d836e612b4fe"}, "docker": "quay.io/biocontainers/sipros", "aliases": {"EnsembleScripts_sipros_ensemble_filtering": "/usr/local/bin/EnsembleScripts_sipros_ensemble_filtering", "EnsembleScripts_sipros_peptides_assembling": "/usr/local/bin/EnsembleScripts_sipros_peptides_assembling", "EnsembleScripts_sipros_prepare_protein_database": "/usr/local/bin/EnsembleScripts_sipros_prepare_protein_database", "EnsembleScripts_sipros_psm_tabulating": "/usr/local/bin/EnsembleScripts_sipros_psm_tabulating", "Raxport": "/usr/local/bin/Raxport", "Raxport.exe": "/usr/local/bin/Raxport.exe", "SiprosEnsembleOMP": "/usr/local/bin/SiprosEnsembleOMP", "SiprosV4OMP": "/usr/local/bin/SiprosV4OMP", "V4Scripts_ClusterSip": "/usr/local/bin/V4Scripts_ClusterSip", "V4Scripts_getLabelPCTinEachFT": "/usr/local/bin/V4Scripts_getLabelPCTinEachFT", "V4Scripts_getSpectraCountInEachFT": "/usr/local/bin/V4Scripts_getSpectraCountInEachFT", "V4Scripts_makeDBforLabelSearch": "/usr/local/bin/V4Scripts_makeDBforLabelSearch", "V4Scripts_refineProteinFDR": "/usr/local/bin/V4Scripts_refineProteinFDR", "V4Scripts_sipros_peptides_assembling": "/usr/local/bin/V4Scripts_sipros_peptides_assembling", "V4Scripts_sipros_peptides_filtering": "/usr/local/bin/V4Scripts_sipros_peptides_filtering", "aprofutil": "/usr/local/bin/aprofutil", "configGenerator": "/usr/local/bin/configGenerator", "copyConfigTemplate": "/usr/local/bin/copyConfigTemplate", "mono-hang-watchdog": "/usr/local/bin/mono-hang-watchdog", "csc": "/usr/local/bin/csc", "csi": "/usr/local/bin/csi", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "vbc": "/usr/local/bin/vbc", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr", "chktrust": "/usr/local/bin/chktrust", "crlupdate": "/usr/local/bin/crlupdate", "csharp": "/usr/local/bin/csharp", "dmcs": "/usr/local/bin/dmcs", "dtd2rng": "/usr/local/bin/dtd2rng", "dtd2xsd": "/usr/local/bin/dtd2xsd", "gacutil": "/usr/local/bin/gacutil", "gacutil2": "/usr/local/bin/gacutil2", "genxs": "/usr/local/bin/genxs", "httpcfg": "/usr/local/bin/httpcfg", "ikdasm": "/usr/local/bin/ikdasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sipros.
singularity registry hpc automated addition for sipros
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sipros
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sipros:4.02--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sipros/4.02--hdfd78af_1
$ module help quay.io/biocontainers/sipros/4.02--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sipros-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sipros-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sipros-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sipros-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sipros-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sipros-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EnsembleScripts_sipros_ensemble_filtering

```bash
$ singularity exec <container> /usr/local/bin/EnsembleScripts_sipros_ensemble_filtering
$ podman run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_ensemble_filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_ensemble_filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnsembleScripts_sipros_peptides_assembling

```bash
$ singularity exec <container> /usr/local/bin/EnsembleScripts_sipros_peptides_assembling
$ podman run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_peptides_assembling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_peptides_assembling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnsembleScripts_sipros_prepare_protein_database

```bash
$ singularity exec <container> /usr/local/bin/EnsembleScripts_sipros_prepare_protein_database
$ podman run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_prepare_protein_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_prepare_protein_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnsembleScripts_sipros_psm_tabulating

```bash
$ singularity exec <container> /usr/local/bin/EnsembleScripts_sipros_psm_tabulating
$ podman run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_psm_tabulating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnsembleScripts_sipros_psm_tabulating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Raxport

```bash
$ singularity exec <container> /usr/local/bin/Raxport
$ podman run --it --rm --entrypoint /usr/local/bin/Raxport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Raxport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Raxport.exe

```bash
$ singularity exec <container> /usr/local/bin/Raxport.exe
$ podman run --it --rm --entrypoint /usr/local/bin/Raxport.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Raxport.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SiprosEnsembleOMP

```bash
$ singularity exec <container> /usr/local/bin/SiprosEnsembleOMP
$ podman run --it --rm --entrypoint /usr/local/bin/SiprosEnsembleOMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SiprosEnsembleOMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SiprosV4OMP

```bash
$ singularity exec <container> /usr/local/bin/SiprosV4OMP
$ podman run --it --rm --entrypoint /usr/local/bin/SiprosV4OMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SiprosV4OMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_ClusterSip

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_ClusterSip
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_ClusterSip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_ClusterSip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_getLabelPCTinEachFT

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_getLabelPCTinEachFT
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_getLabelPCTinEachFT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_getLabelPCTinEachFT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_getSpectraCountInEachFT

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_getSpectraCountInEachFT
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_getSpectraCountInEachFT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_getSpectraCountInEachFT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_makeDBforLabelSearch

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_makeDBforLabelSearch
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_makeDBforLabelSearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_makeDBforLabelSearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_refineProteinFDR

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_refineProteinFDR
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_refineProteinFDR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_refineProteinFDR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_sipros_peptides_assembling

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_sipros_peptides_assembling
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_sipros_peptides_assembling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_sipros_peptides_assembling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### V4Scripts_sipros_peptides_filtering

```bash
$ singularity exec <container> /usr/local/bin/V4Scripts_sipros_peptides_filtering
$ podman run --it --rm --entrypoint /usr/local/bin/V4Scripts_sipros_peptides_filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/V4Scripts_sipros_peptides_filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aprofutil

```bash
$ singularity exec <container> /usr/local/bin/aprofutil
$ podman run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### configGenerator

```bash
$ singularity exec <container> /usr/local/bin/configGenerator
$ podman run --it --rm --entrypoint /usr/local/bin/configGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copyConfigTemplate

```bash
$ singularity exec <container> /usr/local/bin/copyConfigTemplate
$ podman run --it --rm --entrypoint /usr/local/bin/copyConfigTemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copyConfigTemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-hang-watchdog

```bash
$ singularity exec <container> /usr/local/bin/mono-hang-watchdog
$ podman run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csc

```bash
$ singularity exec <container> /usr/local/bin/csc
$ podman run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csi

```bash
$ singularity exec <container> /usr/local/bin/csi
$ podman run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illinkanalyzer

```bash
$ singularity exec <container> /usr/local/bin/illinkanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vbc

```bash
$ singularity exec <container> /usr/local/bin/vbc
$ podman run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-package-runtime

```bash
$ singularity exec <container> /usr/local/bin/mono-package-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sgen-grep-binprot

```bash
$ singularity exec <container> /usr/local/bin/sgen-grep-binprot
$ podman run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al

```bash
$ singularity exec <container> /usr/local/bin/al
$ podman run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al2

```bash
$ singularity exec <container> /usr/local/bin/al2
$ podman run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### caspol

```bash
$ singularity exec <container> /usr/local/bin/caspol
$ podman run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cccheck

```bash
$ singularity exec <container> /usr/local/bin/cccheck
$ podman run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccrewrite

```bash
$ singularity exec <container> /usr/local/bin/ccrewrite
$ podman run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert-sync

```bash
$ singularity exec <container> /usr/local/bin/cert-sync
$ podman run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert2spc

```bash
$ singularity exec <container> /usr/local/bin/cert2spc
$ podman run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certmgr

```bash
$ singularity exec <container> /usr/local/bin/certmgr
$ podman run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chktrust

```bash
$ singularity exec <container> /usr/local/bin/chktrust
$ podman run --it --rm --entrypoint /usr/local/bin/chktrust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chktrust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crlupdate

```bash
$ singularity exec <container> /usr/local/bin/crlupdate
$ podman run --it --rm --entrypoint /usr/local/bin/crlupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crlupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csharp

```bash
$ singularity exec <container> /usr/local/bin/csharp
$ podman run --it --rm --entrypoint /usr/local/bin/csharp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csharp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmcs

```bash
$ singularity exec <container> /usr/local/bin/dmcs
$ podman run --it --rm --entrypoint /usr/local/bin/dmcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtd2rng

```bash
$ singularity exec <container> /usr/local/bin/dtd2rng
$ podman run --it --rm --entrypoint /usr/local/bin/dtd2rng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtd2rng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtd2xsd

```bash
$ singularity exec <container> /usr/local/bin/dtd2xsd
$ podman run --it --rm --entrypoint /usr/local/bin/dtd2xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtd2xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gacutil

```bash
$ singularity exec <container> /usr/local/bin/gacutil
$ podman run --it --rm --entrypoint /usr/local/bin/gacutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gacutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gacutil2

```bash
$ singularity exec <container> /usr/local/bin/gacutil2
$ podman run --it --rm --entrypoint /usr/local/bin/gacutil2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gacutil2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genxs

```bash
$ singularity exec <container> /usr/local/bin/genxs
$ podman run --it --rm --entrypoint /usr/local/bin/genxs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genxs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpcfg

```bash
$ singularity exec <container> /usr/local/bin/httpcfg
$ podman run --it --rm --entrypoint /usr/local/bin/httpcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ikdasm

```bash
$ singularity exec <container> /usr/local/bin/ikdasm
$ podman run --it --rm --entrypoint /usr/local/bin/ikdasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ikdasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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