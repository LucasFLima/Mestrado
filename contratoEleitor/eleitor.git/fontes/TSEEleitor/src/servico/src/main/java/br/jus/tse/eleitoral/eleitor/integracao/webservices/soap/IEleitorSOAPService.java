package br.jus.tse.eleitoral.eleitor.integracao.webservices.soap;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.WebServicesException;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorSituacaoDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.LocalVotacaoDTO;

@WebService(
	targetNamespace = "http://tse.jus.br/eleitoral/eleitor"
)
@SOAPBinding(style = Style.RPC)
public interface IEleitorSOAPService {
	
	@WebMethod
	public EleitorDTO pesquisarEleitorPorInscricao(String inscricao) throws WebServicesException;

	
	@WebMethod
	public LocalVotacaoDTO pesquisarLocalVotacaoPorInscricaoDataNascimentoNomeMae(String inscricao, 
																				   String dataNascimento, 
																				   String nomeMae) 
		throws WebServicesException;

	
	@WebMethod
	public LocalVotacaoDTO pesquisarLocalVotacaoPorNomeDataNascimentoNomeMae(String nomeEleitor, 
																			 Integer dataNascimento, 
																			 String nomeMae) 
		throws WebServicesException;
	
	
	@WebMethod
	public EleitorSituacaoDTO pesquisarSituacao(String inscricao) throws WebServicesException;

}
