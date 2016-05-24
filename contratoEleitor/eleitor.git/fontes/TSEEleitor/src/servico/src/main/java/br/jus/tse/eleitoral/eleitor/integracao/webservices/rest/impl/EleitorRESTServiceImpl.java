package br.jus.tse.eleitoral.eleitor.integracao.webservices.rest.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.WebServicesException;
import br.jus.tse.corporativa.arqjeespring.infra.utils.conversores.ConversorTipoObjeto;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.enums.SituacaoInscricaoEnum;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.managers.IEleitorManager;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.Eleitor;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorSituacaoDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.rest.IEleitorRESTService;

@Service
public class EleitorRESTServiceImpl implements IEleitorRESTService {

	@Autowired
	private IEleitorManager iEleitorManager;

	@Autowired
	private ConversorTipoObjeto conversorTipoObjeto;
	
	@Override
	public EleitorDTO pesquisarPeloId(String pId) throws WebServicesException {
		Eleitor eleitor = null;
		EleitorDTO eleitorDTO = null;
		
		try {
			
			eleitor = iEleitorManager.buscarEleitorPeloNumeroInscricao(pId);
			
			eleitorDTO = conversorTipoObjeto.converter(eleitor, EleitorDTO.class);
			
		} catch (Exception e) {
			throw new WebServicesException("Erro ao pesquisar o eleitor pelo seu id", e);
		}
		
		return eleitorDTO;
	}

	
	@Override
	public EleitorSituacaoDTO pesquisarSituacao(String pId) throws WebServicesException {
		
		Eleitor eleitor = null;
		EleitorSituacaoDTO eleitorSituacaoDTO = null;
		
		try {
			eleitor = iEleitorManager.buscarEleitorPeloNumeroInscricao(pId);
			
			if (eleitor != null) {
			
				eleitorSituacaoDTO = new EleitorSituacaoDTO();
				eleitorSituacaoDTO.setInscricao(eleitor.getId());
				eleitorSituacaoDTO.setNome(eleitor.getNomEleitor());
				eleitorSituacaoDTO.setSituacao(SituacaoInscricaoEnum.valueOf(eleitor.getCodSitEleitor()));
			}
			
		} catch (Exception e) {
			throw new WebServicesException("Erro ao pesquisar o eleitor pelo seu id", e);
		}
		
		return eleitorSituacaoDTO;
	}

}
