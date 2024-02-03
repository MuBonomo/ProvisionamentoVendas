SELECT
    vbeln  AS remessa,
    CASE kvgr5
        WHEN 'ECI' THEN
            'Exp. Clientes Indust'
        WHEN 'EDH' THEN
            'Exportação DSH'
        WHEN 'EED' THEN
            'Exportação Equ.Teste'
        WHEN 'EMO' THEN
            'Exportação OES'
        WHEN 'EXP' THEN
            'Exportação'
        WHEN 'ILO' THEN
            'Indent Locadora'
        WHEN 'NAC' THEN
            'Nacional'
        WHEN 'NCI' THEN
            'Nac. Clientes Indust'
        WHEN 'NDH' THEN
            'Nacional DSH'
        WHEN 'NED' THEN
            'Nacional Equ.Teste'
        WHEN 'NMO' THEN
            'Nacional OES'
        WHEN 'OEE' THEN
            'Exportação - OE'
        WHEN 'OEN' THEN
            'Nacional - OE'
    END as Tipo,
    matnr  AS material,
    lfimg  AS qtd,
    zqvlr  AS valor,
    erdat2 AS dt,
    erzet2 AS hr,
    kunnr  AS cliente
FROM
    mard_dali_bbm.z22v0613_td_ps0
WHERE
        vkorg = 'BR20'
    AND erdat2 BETWEEN '20220101' AND '20230930'
ORDER BY
    erdat2