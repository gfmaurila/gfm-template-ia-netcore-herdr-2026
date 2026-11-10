#Requires -Version 5.1
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$Target = (Join-Path $env:APPDATA 'herdr-core\templates'),
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$source = Join-Path $repoRoot '.herdr\templates'

if (-not (Test-Path -LiteralPath $source)) {
    throw "Diretorio de templates nao encontrado: $source"
}

$templates = Get-ChildItem -LiteralPath $source -Filter 'gfm-*.md' -File
if ($templates.Count -eq 0) {
    throw "Nenhum template gfm-*.md encontrado em $source"
}

if (-not (Test-Path -LiteralPath $Target)) {
    if ($PSCmdlet.ShouldProcess($Target, 'Criar diretorio de templates')) {
        New-Item -ItemType Directory -Path $Target -Force | Out-Null
    }
}

foreach ($template in $templates) {
    $destination = Join-Path $Target $template.Name
    if ((Test-Path -LiteralPath $destination) -and -not $Force) {
        Write-Warning "Ignorado (ja existe): $destination. Use -Force para sobrescrever."
        continue
    }
    if ($PSCmdlet.ShouldProcess($destination, 'Copiar template')) {
        Copy-Item -LiteralPath $template.FullName -Destination $destination -Force:$Force
        Write-Output "Copiado: $($template.Name)"
    }
}

Write-Output "Destino: $Target"
Write-Output "Valide com: hc templates"
