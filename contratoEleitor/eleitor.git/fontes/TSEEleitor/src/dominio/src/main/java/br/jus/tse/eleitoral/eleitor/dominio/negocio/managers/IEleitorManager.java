package br.jus.tse.eleitoral.eleitor.dominio.negocio.managers;

import java.util.Date;
import java.util.List;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.AplicacaoException;
import br.jus.tse.corporativa.arqjeespring.negocio.managers.IBaseCRUDManager;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.Eleitor;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoAgregacao;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTemporario;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTransito;

public interface IEleitorManager extends IBaseCRUDManager<Eleitor, String> {
	
	public Eleitor buscarEleitorPeloNumeroInscricao(String pNumInscricao) throws AplicacaoException;

	public List<Eleitor> buscarEleitorPorDadosEspecialissimos(String pNumInscricao, 
															  Integer pDataNascimentoAsNumber, 
															  String pNomeEleitor, 
															  String pNomePai, 
															  String pNomeMae) 
		throws AplicacaoException;

	
	public Eleitor buscarEleitorPeloNumeroInscricaoDataNascimentoNomeMae(String pNumInscricao, 
																		 Date pDataNascimento, 
																		 String pNomeMae) 
		throws AplicacaoException;

	
	public Eleitor buscarEleitorPeloNomeDataNascimentoNomeMae(String pNomeEleitor, 
															  Integer pDataNascimentoAsNumber, 
															  String pNomeMae) 
		throws AplicacaoException;
		
		
	public ViewLocalVotacaoAgregacao buscarLocalVotacaoAgregacaoEleitor(String pCodObjEleitor) 
		throws AplicacaoException;


	public ViewLocalVotacaoTemporario buscarLocalVotacaoTemporarioEleitor(String pCodObjEleitor) 
		throws AplicacaoException;

	
	public List<ViewLocalVotacaoTransito> buscarLocalVotacaoTransitoEleitor(String pCodObjEleitor) 
		throws AplicacaoException;
	
}
